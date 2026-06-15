import whisper
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tempfile
import os

# ========== CONFIG ==========
SAMPLE_RATE = 16000
BUFFER_SECONDS = 3
CONFIDENCE_THRESHOLD = -0.8
# ============================

model = whisper.load_model("base")
previous_text = ""

# -------- Duplicate helpers --------
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
        if prev_words[i:] == curr_words[:len(prev_words)-i]:
            return " ".join(curr.split()[len(prev_words)-i:])
    return curr

# -------- Audio record --------
def record_audio():
    audio = sd.rec(
        int(BUFFER_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )
    sd.wait()
    return audio.flatten()

print("🎙️ Real-time listening (Ctrl+C to stop)")

try:
    while True:
        audio = record_audio()

        # save temp wav (Whisper needs file)
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

        # ---- DUPLICATE REMOVAL ----
        text = remove_duplicate_words(text)
        text = remove_buffer_overlap(previous_text, text)

        if text:
            print("🧠", text)
            previous_text += " " + text

except KeyboardInterrupt:
    print("\n🛑 Stopped")
