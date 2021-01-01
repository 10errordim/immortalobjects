import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
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
    try:
        with sr.Microphone() as source:
            user = ""
            print("Listening...")
            voice = listener.listen(source)
            user = listener.recognize_google(voice)
            user = user.upper()
            if "IVORY" in user:
                user = user.replace("IVORY", "")
                print(user)
    except:
        pass
    return user


while True:
    user = take_command()
    print(user)
    if "PLAY" in user:
        song = user.replace("PLAY", "")
        talk("Playing " + song)
        talk("Use me again!")
        pywhatkit.playonyt(song)
        break
    elif "TIME" in user:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print("Current time is " + time)
        talk("Current time is " + time)
    elif "TELL ME WHO IS" in user:
        person = user.replace("TELL ME WHO IS", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "DATE" in user:
        talk("Sorry, I have a headache")
    elif "ARE YOU SINGLE" in user:
        talk("I am in a relationship with your wifi")
        print("I am in a relationship with your wifi")
    elif "JOKE" in user:
        talk(pyjokes.get_joke())
    elif "GOODBYE" in user or "BYE" in user:
        break
    else:
        talk("Please say the command again!")
