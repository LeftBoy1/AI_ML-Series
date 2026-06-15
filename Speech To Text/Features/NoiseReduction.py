import sounddevice as sd
import numpy as np
import noisereduce as nr
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
DURATION = 5  # seconds

model = WhisperModel("base", device="cpu", compute_type="int8")

def record_audio():
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )
    sd.wait()
    return audio.flatten()

print("🎙️ Speak...")

# Step 1: Record raw audio
raw_audio = record_audio()

# Step 2: Use first 0.5 sec as noise profile
noise_sample = raw_audio[: int(0.5 * SAMPLE_RATE)]

# Step 3: Apply noise reduction
clean_audio = nr.reduce_noise(
    y=raw_audio,
    y_noise=noise_sample,
    sr=SAMPLE_RATE,
    prop_decrease=1.0
)

# Step 4: Transcribe cleaned audio
segments, info = model.transcribe(clean_audio, language="en")

for seg in segments:
    print("📝:", seg.text)
