from ast import Try
from asyncio import queues
from email.mime import audio
from http import client
#from lib2to3.pytree import _Results
import shutil
import smtplib
from unittest import result
import webbrowser
import speech_recognition  as sr
import pyttsx3
import datetime
import wikipedia
import os
import subprocess



engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 200)
engine.setProperty('volume' , 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voices ', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12 :
        speak("Good Morning  Boss")
        speak("do you had your breakfast")
        a = takeCommand()
        if a == 'yes' :
            speak("okay boss thats great")
        elif a == 'not yet':
            speak("thats not good for your health boss , take care of your diet")
        else :
            speak("please boss firstly eat something")

    elif hour>= 12 and hour<18 :
        speak("Good afternoon Boss")
        speak("boss do you had your lunch")
        b = takeCommand()
        if b == 'yes' :
            speak("okay boss thats great")
        elif b == 'not yet':
            speak("thats not good for your health boss")
        else :
            speak("boss please you should have your lunch first")


    else :
        speak("Good Evening Boss")
        speak("do you had your meal?")
        c = takeCommand()
        if c == 'yes' :
            speak("okay boss thats great")
        elif c == 'not yet':
            speak("thats not good for your health boss")
        else :
            speak("please eat your meal first")

assname =("I am saturday")
speak("HEllo BOss! Its good to see you")
speak(assname)

def username():
    speak("What should i call you ")
    uname = takeCommand()
    speak("Welcome master")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("##########################################".center(columns))
    print("welcome mr." , uname.center(columns))
    print("##########################################".center(columns))

def questions():
    speak("Should i ask a question? boss")
    ans = takeCommand()
    if ans == 'yes' :
        speak("who is the prettiest woman you have ever seen in life")
        her = takeCommand()
        speak(her)
        speak("yeah she is the prettiest")
    elif ans == 'no' :
        speak("boss why you are so rude")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening........")
        audio = r.listen(source)
    try :
        print("Recognizing.......")
        query = r.recognize_google(audio,language='en-in')
        query = query.lower()
        print(f"user said : {query}\n")
    except Exception as e:
        print(e)
        print("unable to recognize")
        return "none"
    
    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()

    server.login('your email id', 'your  email password')
    server.sendmail('your email id' , to, content)
    server.close()

if __name__ == "__main__" :
    clear = lambda : os.system('cls')
    clear()
    wishme()
    username()
    questions()


    while True :

        query = takeCommand()
        
        if 'wikipedia' in query :
            speak('Searching Wikipedia......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("Boss! According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query :
            speak("okay boss ")
            webbrowser.open("www.youtube.in")

    


        #elif "what is" in query or "who is" in query :
           # client = wolframalpha.Client("API__ID")
            #res = client.query(query)
        #try :
            #print(next(res.results).text)
            #speak(next(res.results).text)
        #except StopIteration :
            #print("no results")

