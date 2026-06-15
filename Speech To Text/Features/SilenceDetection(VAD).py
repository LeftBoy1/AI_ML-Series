'''
VAD - Voice Activitiy Detection
Silence ≠ zero sound.
Silence = very low energy for some time.

We compute average volume (energy).

SYNTAX-
        energy = mean(abs(audio))


If energy is below a threshold, user is silent.
'''


'''
1. triggered - it is a state flag.

                False → No speech detected yet (silence mode)
                True → Speech is currently happening
                🔹 Why we need it
                It helps us know when speech starts and ends.

2. vad_mode - Controls how aggressive the silence detection is.
                | Mode | Sensitivity      | Use case                        |
                | ---- | ---------------- | ------------------------------- |
                | 0    | Least aggressive | Studio, very clean audio        |
                | 1    | Mild             | Quiet room                      |
                | 2    | Medium           | Normal environment              |
                | 3    | Most aggressive  | Noisy room (best for mic input) |
                
                
'''

'''
Mic Audio (PyAudio)
   ↓
Frames (frame_duration)
   ↓
VAD (vad_mode)
   ↓
Speech? (True / False)
   ↓
Ring Buffer (collections.deque)
   ↓
triggered = True / False
'''

import webrtcvad        #Detects voice vs silence
import pyaudio          #Handles real-time microphone input.
import collections
import time

# ===================== CONFIG =====================
SAMPLE_RATE = 16000
FRAME_DURATION = 30       # Length of one audio chunk sent to VAD. - ms (10, 20, or 30)
CHANNELS = 1
VAD_MODE = 3              # Aggressiveness (3 = best for noisy rooms)- 0 = least aggressive, 3 = most aggressive
SILENCE_TIMEOUT = 1.0     # Silence duration before stopping(in seconds)
# ==================================================

vad = webrtcvad.Vad(VAD_MODE)

audio = pyaudio.PyAudio()

stream = audio.open(
    format=pyaudio.paInt16,
    channels=CHANNELS,
    rate=SAMPLE_RATE,
    input=True,
    frames_per_buffer=int(SAMPLE_RATE * FRAME_DURATION / 1000),
)

frame_bytes = int(SAMPLE_RATE * FRAME_DURATION / 1000) * 2

ring_buffer = collections.deque(maxlen=10)      #collections.deque only helps us make a decision about speech vs silence.
triggered = False   #Speech state
last_speech_time = None

print("🎤 Listening... Speak something")

try:
    while True:
        frame = stream.read(frame_bytes // 2, exception_on_overflow=False)

        is_speech = vad.is_speech(frame, SAMPLE_RATE)

        if not triggered:
            ring_buffer.append(is_speech)
            if sum(ring_buffer) > 0.8 * ring_buffer.maxlen:
                triggered = True
                ring_buffer.clear()
                print("🟢 Speech started")
        else:
            if is_speech:
                last_speech_time = time.time()
            else:
                if last_speech_time and time.time() - last_speech_time > SILENCE_TIMEOUT:
                    print("🔴 Speech ended (Silence detected)")
                    triggered = False
                    last_speech_time = None

except KeyboardInterrupt:
    print("\n🛑 Stopped")

finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()
