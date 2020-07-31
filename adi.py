import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
      speak("Good Morning!")

    elif hour >=12 and hour<18:
      speak("Good Afternoon!")

    else:
      speak("Good Evening!")

    speak("I am pear Sir.Please tell me how may I help you")

def takeCommand():

   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 1
      audio = r.listen(source)

   try:
       print("Recognizing...")
       query = r.recognize_google(audio, language = "en-in")
       print("User said: ",query)

   except Exception as e:
       print(e)
       print("Say that again please...")
       return "None"
   return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourEmail@gmail.com','your passward')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()
    #less secure app unable goto cosole
#pip install speechRecognition,wikipedia,pyttsx3
if __name__ == "__main__":

 wishMe()
 while True:
   query = takeCommand()
   query = query.lower()

    #logic for executing task based on query
   if 'wikipedia' in query:
      speak("Searching wikipedia...")
      query = query.replace("wikipedia", "")
      results = wikipedia.summary(query, sentences = 2)
      speak("According to wikipedia")
      print(results)
      speak(results)

   elif 'open google' in query:
      webbrowser.open("google.com")

   elif 'open stackoverflow' in query:
      webbrowser.open("stackoverflow.com")

   elif 'play music' in query:
      music_dir = 'D:\\Non Critical\\Songs\\Favorite songs 2'
      songs = os.listdir(music_dir)
      print(songs)
      os.startfile(os.path.join(music_dir,songs[0]))

   elif 'the time' in query:
      strTime = datetime.datetime.now().strftime('%H:%M:%S')
      speak(f"Sir, the time is  (strTime)")

    #copy target from properties
   elif 'open vs code' in query:
      codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code"
      os.startfile(codePath)

   elif 'email' in query:
        try:
            speak("What should I say ?")
            content = takeCommand()
            to = "yourEmail@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry")

   elif 'exit' in query:
        speak('Bye Sir, have a Good day.')
        sys.exit()


   else:
        webbrowser.open('www.google.com')

   speak('Next Command! Sir!')
