#import speech_recognition as sr
from gtts import gTTS
import os
source = input()
tts = gTTS(text=source ,lang='en',slow=False)
tts.save('ct.mp3')
os.system('ct.mp3')
print('Text Converted successfully')

'''r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak: ")
    audio = r.listen(source)
    try:
        output = r.recognize_google(audio)
        print("You said: {}".format(output))
    except:
        print("I can't recognize what you have said.")'''