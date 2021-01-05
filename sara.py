import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices)

engine.setProperty('rate' , -100 )




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning")

    elif hour <=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak(" hey i am sara your assistant how may I help you ")


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio , language='en-in')
        print(f"You said:{query}\n")

    except Exception as e:
        print("say that again please")
        return "None"
    return query




if __name__=="__main__":
    wishme()
    while True:
        query =takecommand().lower()

        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace('wikipedia' ,"")
            results =wikipedia.summary(query , sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play movie" in query:
            speak("which movie to play wait i will decide")
            mo = "E:\\Movies\\English movies"
            movie = os.listdir(mo)
            print(movie)
            os.startfile(os.path.join(mo , movie[1]))
            #os.startfile()
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir , the time is {strTime}")

        elif "quit" in query:
            break




