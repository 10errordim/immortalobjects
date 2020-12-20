from typing import Text
import speech_recognition
import pyttsx3
from gtts import gTTS
import os
from datetime import date, datetime


#saying = pyttsx3.init()
#voices = saying.getProperty('voices')
#rate = saying.getProperty('rate') 
#saying.setProperty('rate', 150)
#saying.setProperty('voice', voices[1].id) 
ear = speech_recognition.Recognizer()
brain = "" #Vì lúc đầu nó có cái beep j đâu

#while True:
with speech_recognition.Microphone() as mic:
    print("IllusOna: Em đang nghe, thưa Ngài!")
    audio = ear.record(mic, duration = 8)

print("IllusOna: . . .")

try:
    you = ear.recognize_google(audio, language='vi-VN')
except:
    you = ""

print("ErrorDIM: " + you)


if you == "":
    brain = "Sao lại không nói gì thế kia... ?"
elif "Xin chào" in you:
    brain = "Xin chào, chủ nhân!"
elif "Nói" in you:
    brain = you
elif "hi" in you:
    brain = "Xin chào, chủ nhân!"
elif "cảm ơn" in you:
    brain = "Không có gì!"
elif "thank you" in you:
    brain = "Your welcome!"
elif "today" in you:
    today = date.today()
    brain = "Today is " + today.strftime("")
elif "Hôm nay là" in you:
    today = date.today()
    brain = "Hôm nay là " + today.strftime("Ngày %d/%m/%Y")
elif "is today" in you:
    today = date.today()
    brain = "Today is " + today.strftime("%d/%m/%Y")
elif "today is" in you:
    today = date.today()
    brain = "Today is " + today.strftime("%d/%m/%Y")
elif "mấy giờ" in you:
    now = datetime.now()
    brain = "Bây giờ là " + now.strftime("%H:%M:%S") + " !"
elif "tạm biệt" in you:
    brain = "Tạm biệt, chủ nhân!"
    print("IllusOna: " + brain)
        #saying.say(brain)
        #saying.runAndWait()
        #break
else:
    brain = "Xin lỗi vì sự thiếu hoàn thiện này, chủ nhân!"


tts = gTTS(text = brain, lang = 'vi')
tts.save("IllusOna.mp3")
os.system("IllusOna.mp3")


print("IllusOna: " + brain)
    #saying.say(brain)
    #saying.runAndWait()
