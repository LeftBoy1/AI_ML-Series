from faster_whisper import WhisperModel

# 1. Load the model (happens once)
model = WhisperModel(
    "base",
    device="cpu",        # use "cuda" if you have GPU
    compute_type="int8"  # lowers CPU usage
)

# 2. Transcribe saved audio file
segments, info = model.transcribe("enemy.mp3")

# 3. Print output
print("Detected language:", info.language)

for segment in segments:
    print(f"[{segment.start:.2f}s → {segment.end:.2f}s] {segment.text}")
