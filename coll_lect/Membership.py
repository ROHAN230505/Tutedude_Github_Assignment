import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognising....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Sorry!! Not Audible"

if __name__ == '__main__':
    print("Pycharm")
    say("Hello I am your Personal Assistant.")
    while True:
        print("Listening.....")
        query = takeCommand()
        sites = [["Chat GPT","https://chatgpt.com/"],
                 ["Google","https://www.google.com/"],
                 ["youtube","https://www.youtube.com/"],
                 ["black box","https://www.blackbox.ai/"],
                 ["My music","https://www.youtube.com/watch?v=sWBKYyh2N7c&list=PLpGf0SBDZZS-47PWF7SDOVb7dOiSrHvSa"]
                 ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

            if f"what is the time" in query:

                h = int(datetime.datetime.now().strftime("%H"))
                if h > 12:
                    h = h - 12
                m = int(datetime.datetime.now().strftime("%M"))
                say(f"Sir the time is{h}   {m}")
        #say(query)