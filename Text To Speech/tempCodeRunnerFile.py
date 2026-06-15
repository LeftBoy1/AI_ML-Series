import asyncio
import edge_tts

async def speak():
    communicate = edge_tts.Communicate(
        text="नमस्ते बोरीस, मैं हिंदी बोल सकता हूँ",
        voice="hi-IN-SwaraNeural"
    )
    await communicate.save("hindi.mp3")

asyncio.run(speak())