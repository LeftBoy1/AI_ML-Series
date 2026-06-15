import sounddevice as sd
import numpy as np
import queue
import threading
import webrtcvad
import noisereduce as nr
from faster_whisper import WhisperModel
import scipy.io.wavfile as wav
import os
import re

# ================= CONFIG =================
SAMPLE_RATE = 16000
CHUNK_DURATION = 0.5  # seconds
WAKE_WORD = "hey boris"
CONFIDENCE_THRESHOLD = 0.6

vad = webrtcvad.Vad(2)  # aggressiveness: 0–3
audio_queue = queue.Queue()

model = WhisperModel("base", compute_type="int8")

# ================= AUDIO CAPTURE =================
def audio_callback(indata, frames, time, status):
    audio_queue.put(indata.copy())

# ================= UTIL FUNCTIONS =================
def is_speech(audio_chunk):
    pcm = (audio_chunk * 32768).astype(np.int16).tobytes()
    return vad.is_speech(pcm, SAMPLE_RATE)

def remove_duplicates(text):
    words = text.split()
    cleaned = [words[0]] if words else []
    for w in words[1:]:
        if w != cleaned[-1]:
            cleaned.append(w)
    return " ".join(cleaned)

def normalize_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# ================= TRANSCRIPTION THREAD =================
def transcriber():
    buffer = []

    while True:
        chunk = audio_queue.get()
        chunk = chunk.flatten()

        # Noise reduction
        chunk = nr.reduce_noise(y=chunk, sr=SAMPLE_RATE)

        if is_speech(chunk):
            buffer.append(chunk)
        else:
            if len(buffer) == 0:
                continue

            audio_data = np.concatenate(buffer)
            buffer.clear()

            wav.write("temp.wav", SAMPLE_RATE, audio_data)

            segments, info = model.transcribe("temp.wav")

            text = ""
            confidence_scores = []

            for seg in segments:
                text += seg.text + " "
                if seg.avg_logprob:
                    confidence_scores.append(np.exp(seg.avg_logprob))

            if not confidence_scores:
                continue

            confidence = sum(confidence_scores) / len(confidence_scores)

            text = normalize_text(text)
            text = remove_duplicates(text)

            if confidence < CONFIDENCE_THRESHOLD:
                print("❌ Low confidence, ignored")
                continue

            if WAKE_WORD in text:
                command = text.replace(WAKE_WORD, "").strip()
                print(f"🟢 Wake word detected")
                print(f"➡ Command: {command}")
            else:
                print(f"🟡 Speech (no wake word): {text}")

            os.remove("temp.wav")

# ================= START =================
stream = sd.InputStream(
    samplerate=SAMPLE_RATE,
    channels=1,
    callback=audio_callback
)

with stream:
    t = threading.Thread(target=transcriber)
    t.daemon = True
    t.start()

    print("🎙 Listening... Press Ctrl+C to stop")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n🛑 Stopped")
