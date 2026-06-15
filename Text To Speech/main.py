import pyttsx3 as ts

engine = ts.init()          # creating TTS engine instance
engine.say('Its just a Test')  # text to speech
engine.runAndWait()







#PROPERTY - rate, volume, voice and voices

print(engine.getProperty('rate'))
print(engine.getProperty('volume'))         #volume should be range from 0 to 1
print(engine.getProperty('voice'))








# Printing names & id of all voices
import pyttsx3 as ts

engine = ts.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice)   
    
    





    
#Changing Voice

import pyttsx3 as ts

engine = ts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.say("hello sir")
engine.runAndWait()






#Saving Voice
import pyttsx3 as ts

engine = ts.init()
engine.save_to_file('hi my name is boris and i am a Airtificial Inteligance', 'boris.mp3')
engine.runAndWait()



#Trying some hindi 
import asyncio
import edge_tts

async def speak():
    communicate = edge_tts.Communicate(
        text="नमस्ते बोरीस, मैं हिंदी बोल सकता हूँ",
        voice="hi-IN-SwaraNeural"
    )
    await communicate.save("hindi.mp3")

asyncio.run(speak())
