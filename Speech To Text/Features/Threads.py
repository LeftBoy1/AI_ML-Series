'''
Without threads:

Recording pauses while transcribing

With threads:

Mic listens continuously

Whisper runs in background
'''

# Thread 1 → Mic + Buffer
# Thread 2 → Transcribe + Logic


import whisper
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tempfile
import os
import threading
import queue
import time

# ========== CONFIG ==========
SAMPLE_RATE = 16000
BUFFER_SECONDS = 3
# ============================

model = whisper.load_model("base")

audio_queue = queue.Queue()
previous_text = ""
running = True

# ---------- Duplicate Removal ----------
def remove_duplicate_words(text):
    words = text.split()
    if not words:
        return ""
    result = [words[0]]
    for w in words[1:]:
        if w.lower() != result[-1].lower():
            result.append(w)
    return " ".join(result)

def remove_buffer_overlap(prev, curr):
    prev_words = prev.lower().split()
    curr_words = curr.lower().split()

    for i in range(len(prev_words)):
        if prev_words[i:] == curr_words[:len(prev_words) - i]:
            return " ".join(curr.split()[len(prev_words) - i:])
    return curr

# ---------- Audio Recording Thread ----------
def audio_recorder():
    while running:
        audio = sd.rec(
            int(BUFFER_SECONDS * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32"
        )
        sd.wait()
        audio_queue.put(audio.flatten())

# ---------- Whisper Transcription Thread ----------
def whisper_worker():
    global previous_text

    while running:
        if audio_queue.empty():
            time.sleep(0.05)
            continue

        audio = audio_queue.get()

        # Whisper needs wav file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            write(f.name, SAMPLE_RATE, audio)
            wav_path = f.name

        result = model.transcribe(
            wav_path,
            language="en",
            condition_on_previous_text=False
        )

        os.remove(wav_path)

        text = result["text"].strip()
        if not text:
            continue

        # ---- Deduplication ----
        text = remove_duplicate_words(text)
        text = remove_buffer_overlap(previous_text, text)

        if text:
            print("🧠", text)
            previous_text += " " + text

# ---------- START ----------
print("🎙️ Real-time Whisper started (Ctrl+C to stop)")

record_thread = threading.Thread(target=audio_recorder)
whisper_thread = threading.Thread(target=whisper_worker)

record_thread.start()
whisper_thread.start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    running = False
    print("\n🛑 Stopped")

