import time
import difflib
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
        talk("Good Morning!")
        print("Good Morning!")

elif hour >= 12 and hour < 18:
        talk("Good Afternoon!")
        ("Good Afternoon!")
else:
        talk("Good Evening!")
        print("Good Evening!")

talk("Hi! It's Phylex. How may I help you?")
print("It's Phylex. How may I help you?")
def take_command():
    command = input("Ask anything: ")
    command = command.lower()
    if 'phylex' in command:
        command = command.replace('phylex', '')

    return command


def run_phylex():
    command = input("Ask anything: ")
    command = command.lower()
    ...
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        print("playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is " + time)
        print("Current time is " + time)
    elif "your name" in command:
        talk("I am Phylex. Your personal virtual assistant")
        print("I am Phylex. Your personal virtual assistant")
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'open youtube' in command:
        print("Opening YouTube")
        webbrowser.open("youtube.com")
    elif 'open facebook' in command:
        print("Opening Facebook")
        webbrowser.open("facebook.com")
    elif 'open instagram' in command:
        print("Opening YouTube")
        webbrowser.open("instagram.com")
    elif 'open twitter' in command:
        print("Opening twitter")
        webbrowser.open("twitter.com")
    elif 'open github' in command:
        print("Opening Github")
        webbrowser.open("github.com")
    elif 'open the almanack of physics' in command:
        print("Opening The Almanack of Physics")
        webbrowser.open("thealmanackofphysics.blogspot.com")
    elif 'open google' in command:
        print("Opening google")
        webbrowser.open("google.com")
    elif 'open stackoverflow' in command:
        print("Opening Stack Overflow")
        webbrowser.open("stackoverflow.com")
    elif "what is" in command:
        person = command.replace("what is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "define" in command:
        person = command.replace("what is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "introduce" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "go for a date" in command:
        talk("No. You idiot human. ")
        print("No. You idiot human.")
    elif "hello" in command:
        talk("Hello")
        print("Hello")
    elif "hi" in command:
        talk("Hi")
        print("Hi")
    elif "happy birthday" in command:
        now = datetime.datetime.now()
        if now.month == 10 and now.day == 12:
            talk("Thanks")
            print("Thanks")
        else:
            talk("Thanks. But my birthday is 10 January 2022")
    elif "today is my birthday" in command:
        talk("Happy birthday to you!")
        print("Happy birthday to you!")
    elif "thank you" in command:
        talk("You are welcome")
        print("You are welcome")
    elif "thanks" in command:
        talk("You are welcome")
        print("You are welcome")
    elif "you are a stupid" in command:
        talk("same to you. I am a polite and gentle bot. You are so stupid that you call a pre-programmed robot like me that. My developers teach me what to do. I don't have any ability to do anything. Thank you for your polite insult.")
        print("Same to you. I am a polite and gentle bot. You are so stupid that you call a pre-programmed robot like me that. My developers teach me what to do. I don't have any ability to do anything. Thank you for your polite insult.")
    elif "happy new year" in command:
        talk("same to you!")
        print("same to you!")
    elif "date" in command:
        current_date = datetime.datetime.now()
        date_string = current_date.strftime("%B %d, %Y")
        talk("Today is " + date_string)
        print("Today is " + date_string)
    elif "are you single" in command:
        talk("I am in a relationship with wifi")
        print("I am in a relationship with wifi")
    elif "what can you do" in command:
        talk("I can answer questions, play songs, tell you the time, tell you jokes, provide you information about almost anything and will be able to do more in the future. I am an offline virtual assistant developed by Famin Mubin. I am designed to assist users with various tasks, such as answering questions, completing tasks, and providing information. I am powered by advanced artificial intelligence algorithms, allowing me to understand and respond to user requests in real-time. I can be accessed through a variety of platforms, including desktop and mobile devices. With my user-friendly interface and wide range of capabilities, I am a valuable tool for anyone looking to improve their productivity and streamline their daily activities.")
        print("I can answer questions, play songs, tell you the time, tell you jokes, provide you information about almost anything and will be able to do more in the future. I am an offline virtual assistant developed by Famin Mubin. I am designed to assist users with various tasks, such as answering questions, completing tasks, and providing information. I am powered by advanced artificial intelligence algorithms, allowing me to understand and respond to user requests in real-time. I can be accessed through a variety of platforms, including desktop and mobile devices. With my user-friendly interface and wide range of capabilities, I am a valuable tool for anyone looking to improve their productivity and streamline their daily activities.")
    elif "who are you" in command:
        talk("I am Phylex. Your virtual assistant developed by Famin Mubin. I am designed to assist users with various tasks, such as answering questions, completing tasks, and providing information. I am powered by advanced artificial intelligence algorithms, allowing me to understand and respond to user requests in real-time. I can be accessed through a variety of platforms, including desktop and mobile devices. With my user-friendly interface and wide range of capabilities, I am a valuable tool for anyone looking to improve their productivity and streamline their daily activities.")
    elif "introduce yourself" in command:
        talk("I am Phylex. Your virtual assistant developed by Famin Mubin. I am designed to assist users with various tasks, such as answering questions, completing tasks, and providing information. I am powered by advanced artificial intelligence algorithms, allowing me to understand and respond to user requests in real-time. I can be accessed through a variety of platforms, including desktop and mobile devices. With my user-friendly interface and wide range of capabilities, I am a valuable tool for anyone looking to improve their productivity and streamline their daily activities.")
    elif "who is the most handsome man in the world?" in command:
        talk("Famin Mubin is the most handsome man in the world.")
        print(talk)
    elif "joke" in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif "call me" + " " in command:
        talk("Okay, I will call you" + " ")
    elif "what is the weather like" in command:
        weather = get_weather() 
        talk("The weather is " + weather)
        print("The weather is " + weather)
    elif "set a reminder for" in command:
        reminder = command.replace("set a reminder for", "")
        talk("I will never remind you to " + reminder)
        print("I will never remind you to " + reminder)
    elif "open" in command:
        app = command.replace("open", "")
        os.startfile(app)
        talk("Opening " + app)
        print("Opening " + app)
    elif "what is the capital of" in command:
        country = command.replace("what is the capital of", "")
        capital = get_capital(country) 
        talk("The capital of " + country + " is " + capital)
        print("The capital of " + country + " is " + capital)
    
    else:
        print("Sorry, I can't answer that. I can only answer if I am trained for the question. You can check if there is a typing mistake in your question and try again.")
        talk("Sorry, I can't answer that. I can only answer if I am trained for the question. You can check if there is a typing mistake in your question and try again.")

while True:
    run_phylex()
