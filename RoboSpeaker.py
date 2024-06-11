import pyttsx3 #text to speech library

if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1. Created by Mariam")
    engine = pyttsx3.init() #initialize text to speech engine
    while True:
        x= input("Enter what you want me to say: ")
        if x == 'q':
            break
        engine.say(x) #use engine to say the given text
        engine.runAndWait() # wait for speech to be completed 