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
            if "IVORY SAY" in user:
                user = user.upper().replace("IVORY SAY", "")
                print(user)
    except:
        pass
    return user


def main_program():
    while True:
        user = take_command()
        print(user)
        if "PLAY" in user.upper():
            song = user.upper().replace("PLAY", "")
            print("PLaying", song)
            talk("Playing " + song)
            print("Use me again!")
            talk("Use me again!")
            pywhatkit.playonyt(song)
            break
        elif "TIME" in user.upper():
            now = datetime.now()
            print("It is " + now.strftime("%H hours %M minutes %S seconds") + " by now.")
            talk("It is " + now.strftime("%H hours %M minutes %S seconds") + " by now.")
        elif "WHO IS" in user.upper():
            person = user.upper().replace("WHO IS", "")
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif "TODAY IS" in user.upper() or "IS TODAY" in user.upper():
            today = date.today()
            dateinfo = "Today is " + today.strftime("%B %d, %Y")
            print(dateinfo)
            talk(dateinfo)
        elif "ARE YOU SINGLE" in user.upper():
            print("I am in a relationship with your wifi.")
            talk("I am in a relationship with your wifi.")
        elif "JOKE" in user.upper():
            print(pyjokes.get_joke())
            talk(pyjokes.get_joke())
        elif "GOODBYE" in user.upper() or "BYE" in user.upper():
            print("Goodbye!")
            talk("Goodbye!")
            break
        elif "THANKS" in user.upper() or "THANK YOU" in user.upper():
            print("Your wellcome")
            talk("Your wellcome")
        elif "I LOVE YOU" in user.upper():
            print("I love you too!")
            talk("I love you too!")
        else:
            print("Please say the command again!")
            talk("Please say the command again!")


main_program()
