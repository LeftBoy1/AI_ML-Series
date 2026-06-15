
'''
CHUNKS - A small piece of audio cut from a continuous sound stream
Example - 
            Imagine someone speaking for 20 seconds.

            You cannot hand the entire 20 seconds to Whisper while it's still being spoken.

            So you do this instead:

            Second 1-4   → chunk 1
            Second 5-8   → chunk 2
            Second 9-12  → chunk 3
            ...


            Each chunk = one short recording
'''


'''
audio.flatten() - It converts a 2D audio array into a 1D array. Because ,Human speech is mono and mono needs 1D audio.
If we not use audio.flatten() then it occurs -
                                                Error
                                                Wrong transcription
                                                Silent output
                                                Unexpected behavior
                                                

'''


import sounddevice as sd    #used To capture sound from the microphone into Python.
from scipy.io.wavfile import write  #used To save recorded audio into a WAV file.
from faster_whisper import WhisperModel
import os


SAMPLE_RATE = 16000 #Sample rate controls how detailed your audio is.
DURATION = 4  # seconds per chunk

# Load Whisper model once
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("🎙️ Real-time listening... Press CTRL+C to stop.")

try:
    while True:
        # 1. Record audio chunk
        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),        # How much audio to record
            samplerate=SAMPLE_RATE,             #Audio resolution
            channels=1,                         #Mono audio {Human speech is mono}
            dtype='float32'                     #How audio is stored
        )
        sd.wait()
        
        audio = audio.flatten() #convert 2D to 1D

        # 2. Save chunk temporarily
        write("temp.wav", SAMPLE_RATE, audio)

        # 3. Transcribe chunk
        segments, _ = model.transcribe("temp.wav")

        # 4. Print partial output
        for segment in segments:
            print("🗣️", segment.text)

        print("-" * 30)

except KeyboardInterrupt:
    print("\n🛑 Stopped listening")
    if os.path.exists("temp.wav"):
        os.remove("temp.wav")
