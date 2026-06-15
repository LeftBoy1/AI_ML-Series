'''
Audio buffering =
👉 You don’t wait for the user to finish speaking completely
👉 You capture audio in small chunks (e.g. 2–5 seconds)
👉 Each chunk is processed immediately

Think of it like reading a sentence word-by-word instead of waiting for the whole paragraph.
'''

from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np

model = WhisperModel("base", device="cpu", compute_type="int8")

SAMPLE_RATE = 16000
BUFFER_DURATION = 4  # seconds

def record_audio():
    audio = sd.rec(
        int(BUFFER_DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )
    sd.wait()
    return audio.flatten()

while True:
    print("🎧 Listening...")
    audio = record_audio()

    segments, _ = model.transcribe(
        audio,
        language="en"
    )

    for segment in segments:
        print("🧠:", segment.text)
