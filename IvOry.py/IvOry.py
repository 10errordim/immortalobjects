import speech_recognition
import pyttsx3
from datetime import date, datetime


saying = pyttsx3.init()
voices = saying.getProperty('voices')
rate = saying.getProperty('rate')
saying.setProperty('rate', 150)
saying.setProperty('voice', voices[1].id) 
ear = speech_recognition.Recognizer()
brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("IllusOna: I'm listening, Master")
        audio = ear.listen(mic)

    print("IllusOna: . . .")

    try:
        you = ear.recognize_google(audio)
    except:
        you = ""

    print("ErrorDIM: " + you)


    if you == "":
        brain = "I can't really hear you well, please say again, Master!"
    elif "hello" in you:
        brain = "Greetings, Master!"
    elif "hi" in you:
        brain = "Greetings, Master!"
    elif "thanks" in you:
        brain = "Your welcome!"
    elif "thank you" in you:
        brain = "Your welcome!"
    elif "today" in you:
        today = date.today()
        brain = "Today is " + today.strftime("%B %d, %Y")
    elif "date is today" in you:
        today = date.today()
        brain = "Today is " + today.strftime("%B %d, %Y")
    elif "is today" in you:
        today = date.today()
        brain = "Today is " + today.strftime("%B %d, %Y")
    elif "today is" in you:
        today = date.today()
        brain = "Today is " + today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        brain = "It is " + now.strftime("%H hours %M minutes %S seconds") + " by now. Master!"
    elif "goodbye" in you:
        brain = "Bye, Master!"
        print("IllusOna: " + brain)
        saying.say(brain)
        saying.runAndWait()
        break
    else:
        brain = "I'm sorry for this uncompletement, Master!"

    print("IllusOna: " + brain)
    saying.say(brain)
    saying.runAndWait()
