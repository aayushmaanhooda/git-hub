import pyttsx3
import speech_recognition as sr
import os

def take_commands():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold =0.7
        audio = r.listen(source)

        try:
            print("recognizing")
            q = r.recognize_google(audio)
            print("printing your reply='", q , "'")

        except Exception as e:
            print(e)
            print("say that again sir")
            return "None"
        import time
        time.sleep(2)
        return q

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

speak("do you want to shutdown your computer sir")
while True:
    command = take_commands()
    if "no" in command:
        speak("thank u sir i will not shut down ur pc")
        break
    if "yes" in command:
        command.speak("shutting ur pc")
        os.system("shutdown /s /t 30")
    speak("say again")

