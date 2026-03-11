import pyttsx3
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
        return query.lower()

    except:
        return "none"

def runAssistant():
    while True:
        query = takeCommand()

        if "hello" in query:
            speak("Hello, how can I help you")

        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            webbrowser.open("https://google.com")