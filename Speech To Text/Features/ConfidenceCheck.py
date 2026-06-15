'''
We use 3 main signals:

1️⃣ avg_logprob (MOST IMPORTANT)

                                Measures how confident the model is about its words
                                Higher (closer to 0) = more confident

2️⃣ no_speech_prob

                    Probability that the audio is actually silence/noise
                    High value = bad transcription

3️⃣ Text quality heuristics

                            Very short text
                            Repeated words
                            Garbage symbols
'''

'''
| avg_logprob    | Confidence |
| -------------- | ---------- |
| `>-0.4`        | 🟢 High    |
| `-0.4 to -0.8` | 🟡 Medium  |
| `< -0.8`       | 🔴 Low     |
'''

from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np

model = WhisperModel("base", device="cpu", compute_type="int8")

SAMPLE_RATE = 16000
DURATION = 4  # seconds

def record_audio():
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )
    sd.wait()
    return audio.flatten()

def confidence_from_logprob(avg_logprob):
    if avg_logprob > -0.4:
        return "HIGH"
    elif avg_logprob > -0.8:
        return "MEDIUM"
    else:
        return "LOW"

audio = record_audio()

segments, info = model.transcribe(audio, language="en")

for seg in segments:
    confidence = confidence_from_logprob(seg.avg_logprob)

    print("📝 Text:", seg.text)
    print("📊 avg_logprob:", round(seg.avg_logprob, 3))
    print("✅ Confidence:", confidence)
    print("-" * 40)
