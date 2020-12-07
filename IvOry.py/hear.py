import speech_recognition

ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("IllusOna: I'm listening, Master")
    audio = ear.listen(mic)

try:
    you = ear.recognize_google(audio)
except:
    you = ""

print("ErrorDIM: " + you)