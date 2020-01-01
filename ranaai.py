import sys
import pyttsx3 
import datetime
import wikipedia
import webbrowser
# import PyAudio
import speech_recognition as sr
import smtplib
# initialisation 
engine = pyttsx3.init() 
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
# hour=int(datetime.datetime.now().hour)
# print(hour)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour<=18:
        speak("good evening")
    elif hour>=18 and hour<24:
        speak("good night")
    speak("I am rana Assistant! tell me how can i help you")
    


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('enter your gmail here', 'type your password here')
    server.sendmail('enter your gmail here', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        print(query)
    
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Rana Atul, the time is {Time}")
        elif 'email to nanda' in query:
            try:
                speak("Kya bhejna hai email")
                content = takeCommand()
                to = "rn045942@gmail.com"    
                sendEmail(to, content)
                speak("Email sent!")
            except Exception as e:
                print(e)
                speak("Sorry some error")
    
