from http import server
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hi I'm Jarvis Ma'am. Please tell me how I may help you?")

def takeCommand():
    # it takes microsoft input from the user and returns string output

    r= sr.Recognizer() #recognizer helps in recognizing the audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio= r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language="en.in")
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content): #email send krne keliye less secure apps ko enable krna hoga gmail mai
    server= smtplib.SMTP("smntp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com","your-password") #password ko text file ami likhen or wahn se read krke program mai layen direct nhi security issues ki wajah se
    server.sendmail("youremail@gmail.com",to,content) #yor email an dpassword ki jagah pr apke gmail or pass ayega
    server.close()

if __name__=="__main__":
    # speak("Mariam is a good girl.")
    wishMe()
    while True:
    # if 1:
        query= takeCommand().lower()

        #logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences= 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        # elif 'play music' in query:
        #     music_dir= "D:\\Non critical\\songs\\"
        #     songs= os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, the time is {strTime}")
        
        elif 'open vs' in query:
            codePath= "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to maryam' in query:
            try:
                speak("What should I say?")
                content= takeCommand()
                to="mariamyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I'm not able to send this email.")

        elif 'exit jarvis' in query:
            quit() 