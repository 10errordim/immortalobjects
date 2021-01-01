import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import date, datetime
import wikipedia
import pyjokes


iding = 0
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    user = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            talk("Listening...")
            voice = listener.listen(source)
            user = listener.recognize_google(voice)
            user = user.upper()
            if "IVORY SAY" in user:
                user = user.replace("IVORY SAY", "")
                print(user)
    except:
        pass
    return user


while True:
    user = take_command()
    print(user)
    if "PLAY" in user:
        song = user.replace("PLAY", "")
        print("PLaying", song)
        talk("Playing " + song)
        print("Use me agian!")
        talk("Use me again!")
        pywhatkit.playonyt(song)
        break
    elif "TIME" in user:
        now = datetime.now()
        print("It is " + now.strftime("%H hours %M minutes %S seconds") + " by now.")
        talk("It is " + now.strftime("%H hours %M minutes %S seconds") + " by now.")
    elif "WHO IS" in user:
        person = user.replace("WHO IS", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "TODAY IS" in user or "IS TODAY" in user:
        today = date.today()
        dateinfo = "Today is " + today.strftime("%B %d, %Y")
        print(dateinfo)
        talk(dateinfo)
    elif "ARE YOU SINGLE" in user:
        print("I am in a relationship with your wifi.")
        talk("I am in a relationship with your wifi.")
    elif "JOKE" in user:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif "GOODBYE" in user or "BYE" in user:
        print("Goodbye!")
        talk("Goodbye!")
        break
    elif "THANKS" in user or "THANK YOU" in user:
        print("Your wellcome")
        talk("Your wellcome")
    else:
        print("Please say the command again!")
        talk("Please say the command again!")
