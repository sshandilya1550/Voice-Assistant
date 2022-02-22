import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import sys
import subprocess
import pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha
import time
import ssl
from subprocess import call
import sqlite3
from tkinter import *
import pathlib


def assistant():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    wolframalpha_app_id = 'GUQ54U-A7TA45YELQ'
    ssl._create_default_https_context = ssl._create_unverified_context

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def time_():
        Time = datetime.datetime.now().strftime("%H:%M:%S")  # for 24 hour clock
        speak("The current time is")
        speak(Time)

    def date_():
        today = datetime.date.today()
        d2 = today.strftime("%B %d, %Y")
        speak("The current date is")
        speak(d2)

    def wishme():
        speak("Hello Sir!")

        # Some Gretings
        hour = datetime.datetime.now().hour
        if hour >= 6 and hour < 12:
            speak("Good Morning!")

        elif hour >= 12 and hour < 18:
            speak("Good Afternoon!")

        elif hour >= 18 and hour < 24:
            speak("Good Evening!")
        else:
            speak("It's too late!")

        speak("Please tell me how can I help you today?")

    def TakeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-us')
            print(query)

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.ehlo()
        server.starttls()
        server.login('sshandilya2030@gmail.com', 'Python@1234')
        server.sendmail('sshandilya2030@gmail.com', to, content)
        server.close()

    def screenshot():
        call(["screencapture", "screenshot.jpg"])
        speak("Done Sir!")

    def cpu():
        usage = str(psutil.cpu_percent())
        speak('CPU is at'+usage)

        battery = psutil.sensors_battery()
        speak('Battery is at')
        speak(battery.percent)

    def joke():
        speak(pyjokes.get_joke())

    def user_data():
        conn = sqlite3.connect("record.sqlite")
        cur = conn.cursor()
        last_row = cur.execute('select * from Login').fetchall()[-1]
        print(last_row)
        conn.commit()
        conn.close()

    if __name__ == "__main__":
        wishme()
        while True:
            query = TakeCommand().lower()

            if 'time' in query:  # tell us time when asked
                time_()

            if 'date' in query:  # tell us date when asked
                date_()

            elif 'wikipedia' in query:
                speak("Searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=3)
                speak('According to Wikipedia')
                print(result)
                speak(result)

            elif 'send an email' in query:
                try:
                    speak("What should I say?")
                    content = TakeCommand()
                    # provide receiver email address

                    speak("Who is the Receiver?")
                    receiver = input("Enter Receiver's Email:")
                    to = receiver
                    sendEmail(to, content)
                    speak(content)
                    speak('Email has been sent.')

                except Exception as e:
                    print(e)
                    speak("Unable to send Email.")

            elif 'open stack overflow' in query:
                speak("Opening sir...")
                wb.open("https://stackoverflow.com/")

            elif 'open my class' in query:
                speak("Opening sir...")
                wb.open('https://myclass.lpu.in/')

            elif 'whatsapp' in query:
                speak("Opening sir...")
                wb.open('https://web.whatsapp.com/')

            elif 'search in chrome' in query:
                speak('What should I search?')
                chrome_path = r"open -a /Applications/Google\ Chrome.app %s"
                search = TakeCommand().lower()
                wb.get(chrome_path).open("http://"+search+".com")

            elif 'search youtube' in query:
                speak('What should I search?')
                search_Term = TakeCommand().lower()
                speak("Here we go to YOUTUBE!")
                wb.open('https://www.youtube.com/search?q='+search_Term)

            elif 'search google' in query:
                speak('What should I search?')
                search_Term = TakeCommand().lower()
                speak("Searching...")
                wb.open('https://www.google.com/search?q='+search_Term)

            elif 'cpu' in query:
                cpu()

            elif 'joke' in query:
                joke()

            elif "last user" in query:
                user_data()

            elif 'go offline' in query:
                speak("Going offline Sir! Hope to see you soon")
                quit()

            elif 'ms word' in query:
                speak('Opening MS Word Sir...')
                os.system(r"open /Applications/Microsoft\ Word.app")

            elif 'safari' in query:
                speak('Opening safari Sir...')
                os.system(r"open /Applications/Safari.app")

            elif 'write a note' in query:
                speak("What should I write, Sir?")
                notes = TakeCommand()
                file = open('mytext.txt', 'w')
                speak("Sir should I include Date and Time?")
                ans = TakeCommand()
                if 'yes' in ans or 'sure' in ans:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(':-')
                    file.write(notes)
                    speak("Done Taking Notes, Sir!")
                else:
                    file.write(notes)

            elif 'show note' in query:
                speak('Showing notes')
                file = open('mytext.txt', 'r')
                print(file.read())
                speak(file.read())

            elif 'capture screenshot' in query:
                screenshot()

            elif 'who are you' in query:
                speak(
                    "I am Ank. I'm created by Satyam Shandilya. I'm a Personal Assistant.")

            elif 'how are you' in query:
                speak(
                    "I am Fine Sir. Hope you are fine too")

            elif 'play music' in query:
                songs_dir = r'/Users/satyamshandilya/Project/Song'
                music = os.listdir(songs_dir)
                speak('What should I play?')
                speak('Select a number...')
                ans = TakeCommand().lower()
                while('number' not in ans and ans != 'random' and ans != 'you choose'):
                    speak('I could not understand you. Please Try Again!')
                    ans = TakeCommand().lower()
                if 'number' in ans:
                    no = int(ans.replace('number', ''))
                elif 'random' or 'you choose' in ans:
                    no = random.randint(1, 4)
                path = os.path.join(songs_dir, music[no])
                subprocess.Popen(['mpg123', '-q', path]).wait()

            elif 'remember that' in query:
                speak("What should I remember?")
                memory = TakeCommand()
                remember = open('memory.txt', 'w')
                remember.write(memory)
                remember.close()
                speak("You asked me to remember that"+memory)

            elif 'do you remember' in query:
                remember = open('memory.txt', 'r')
                speak('You asked me to remember that'+remember.read())

            elif 'news' in query:
                try:
                    jsonObj = urlopen(
                        "http://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=db044e694b09429e85f7c790229dc0af")
                    data = json.load(jsonObj)
                    i = 1

                    speak('Here are some top headlines of the General News')
                    print('==========TOP HEADLINES=========='+'\n')
                    for item in data['articles']:
                        print(str(i)+'. '+item['title']+'\n')
                        print(item['description']+'\n')
                        speak(item['title'])
                        i += 1
                except Exception as e:
                    print(str(e))

            elif 'where is' in query:
                query = query.replace("where is", "")
                location = query
                speak("user asked to locate"+location)
                wb.open_new_tab("https://www.google.com/maps/place/"+location)

            elif 'calculate' in query:
                client = wolframalpha.Client(wolframalpha_app_id)
                index = query.lower().split().index('calculate')
                query = query.split()[index+1:]
                res = client.query(''.join(query))
                answer = next(res.results).text
                print('The Answer is:'+answer)
                speak('The Answer is:'+answer)

            elif 'what is' in query or 'who is' in query:
                client = wolframalpha.Client(wolframalpha_app_id)
                res = client.query(query)
                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No Results")

            elif 'wait' in query:
                inp = input("press enter")
                if inp == "":
                    time.sleep(1)
                time.sleep(1)

            elif 'log out' in query:
                os.system("shutdown -1")

            elif 'restart' in query:
                os.system("shutdown /r /t 1")

            elif 'shutdown' in query:
                os.system("shutdown /s /t 1")


def data():
    conn = sqlite3.connect("/Users/satyamshandilya/Project/record.sqlite")
    cur = conn.cursor()
    cur.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Login' ''')
    if cur.fetchone()[0] == 0:
        cur.execute("CREATE TABLE Login(Username TEXT, Date TEXT, Time TEXT)")
    date = datetime.date.today()
    time = datetime.datetime.now().strftime("%H:%M:%S")
    global user_name
    user_name = userentry
    cur.execute("INSERT INTO Login(Username,Date,Time) VALUES (?,?,?)",
                (user_name, date, time))
    conn.commit()
    conn.close()
    assistant()


def signup():
    global signup_screen
    signup_screen = Toplevel(main_screen)
    signup_screen.title("Sign Up")
    signup_screen.configure(bg="#87ceeb")
    signup_screen.resizable(False, False)
    window_height = 450
    window_width = 450
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2)-150)
    signup_screen.geometry("{}x{}+{}+{}".format(window_width,
                                                window_height, x_cordinate, y_cordinate))
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(signup_screen, text="Please enter details below", bg="#977EF2", width="300",
          height="2", font=("Calibri", 15)).pack()
    Label(signup_screen, text="", bg="#87ceeb").pack()
    username_lable = Label(signup_screen, text="Username * ", bg="#F25C05", width=15,
                           height=1, font=("Calibri", 13))
    username_lable.pack()
    username_entry = Entry(signup_screen, textvariable=username)
    username_entry.pack()
    Label(signup_screen, text="", bg="#87ceeb").pack()
    password_lable = Label(signup_screen, text="Password * ", bg="#F25C05", width=15,
                           height=1, font=("Calibri", 13))
    password_lable.pack()
    password_entry = Entry(signup_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(signup_screen, text="", bg="#87ceeb").pack()
    Label(signup_screen, text="", bg="#87ceeb").pack()
    Button(signup_screen, text="Sign Up", width=15,
           height=2, command=signup_user, highlightbackground="#F25C05", font=("Calibri", 13)).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.configure(bg="#87ceeb")
    login_screen.resizable(False, False)
    window_height = 450
    window_width = 450
    screen_width = login_screen.winfo_screenwidth()
    screen_height = login_screen.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2)-150)
    login_screen.geometry("{}x{}+{}+{}".format(window_width,
                                               window_height, x_cordinate, y_cordinate))
    Label(login_screen, text="Please enter details below to login", bg="#977EF2", width="300",
          height="2", font=("Calibri", 15)).pack()
    Label(login_screen, text="", bg="#87ceeb").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ", bg="#F25C05", width=15,
          height=1, font=("Calibri", 13)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="", bg="#87ceeb").pack()
    Label(login_screen, text="Password * ", bg="#F25C05", width=15,
          height=1, font=("Calibri", 13)).pack()
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="", bg="#87ceeb").pack()
    Label(login_screen, text="", bg="#87ceeb").pack()
    Button(login_screen, text="Login", width=15,
           height=2, command=login_verify, highlightbackground="#F25C05", font=("Calibri", 13)).pack()

# Implementing event on Signup button


def signup_user():

    username_info = username.get()
    password_info = password.get()
    dir1 = pathlib.Path(__file__).parent.absolute()
    dir2 = os.path.join(dir1, username_info)
    file = open(dir2, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    global signup_success_screen
    signup_success_screen = Toplevel(signup_screen)
    signup_success_screen.title("Sign Up Success")

    signup_success_screen.configure(bg="#87ceeb")
    signup_success_screen.resizable(False, False)
    window_height = 450
    window_width = 450
    screen_width = signup_success_screen.winfo_screenwidth()
    screen_height = signup_success_screen.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2)-150)
    signup_success_screen.geometry("{}x{}+{}+{}".format(window_width,
                                                        window_height, x_cordinate, y_cordinate))
    Label(signup_success_screen, text="", bg="#87ceeb").pack()
    Label(signup_success_screen, text="", bg="#87ceeb").pack()

    Label(signup_success_screen, text="Sign Up Successful", bg="#F25C05", width=20,
          height=2, font=("Calibri", 18)).pack()
    Label(signup_success_screen, text="", bg="#87ceeb").pack()

    Button(signup_success_screen, text="OK",
           command=login,  width=5,
           height=2, highlightbackground="#F25C05", font=("Calibri", 13)).pack()

# Implementing event on login button


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    global userentry
    userentry = username1
    dir1 = pathlib.Path(__file__).parent.absolute()
    dir2 = os.path.join(dir1, username1)
    list_of_files = os.listdir(dir1)
    if username1 in list_of_files:
        file1 = open(dir2, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Login Success")

    login_success_screen.configure(bg="#87ceeb")
    login_success_screen.resizable(False, False)
    window_height = 450
    window_width = 450
    screen_width = login_success_screen.winfo_screenwidth()
    screen_height = login_success_screen.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2)-150)
    login_success_screen.geometry("{}x{}+{}+{}".format(window_width,
                                                       window_height, x_cordinate, y_cordinate))
    Label(login_success_screen, text="", bg="#87ceeb").pack()
    Label(login_success_screen, text="", bg="#87ceeb").pack()

    Label(login_success_screen, text="Login Successful", bg="#F25C05", width=20,
          height=2, font=("Calibri", 18)).pack()
    Label(login_success_screen, text="", bg="#87ceeb").pack()

    Button(login_success_screen, text="OK",
           command=data,  width=5,
           height=2, highlightbackground="#F25C05", font=("Calibri", 13)).pack()

# Designing popup for login invalid password


def password_not_recognised():

    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.configure(bg="#87ceeb")
    login_screen.resizable(False, False)
    window_height = 450
    window_width = 450
    screen_width = login_screen.winfo_screenwidth()
    screen_height = login_screen.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2)-150)
    login_screen.geometry("{}x{}+{}+{}".format(window_width,
                                               window_height, x_cordinate, y_cordinate))
    Label(login_screen, text="Please enter details below to login", bg="#977EF2", width="300",
          height="2", font=("Calibri", 15)).pack()
    Label(login_screen, text="", bg="#87ceeb").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ", bg="#F25C05", width=15,
          height=1, font=("Calibri", 13)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="", bg="#87ceeb").pack()
    Label(login_screen, text="Password * ", bg="#F25C05", width=15,
          height=1, font=("Calibri", 13)).pack()
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="", bg="#87ceeb").pack()
    Label(login_screen, text="", bg="#87ceeb").pack()
    Button(login_screen, text="Login", width=15,
           height=2, command=login_verify, highlightbackground="#F25C05", font=("Calibri", 13)).pack()

    Label(login_screen, text="", bg="#87ceeb").pack()
    Label(login_screen, text="Invalid Password",
          fg="red", font=("calibri", 14)).pack()

# Designing popup for user not found


def user_not_found():

    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.configure(bg="#87ceeb")
    login_screen.resizable(False, False)
    window_height = 450
    window_width = 450
    screen_width = login_screen.winfo_screenwidth()
    screen_height = login_screen.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2)-150)
    login_screen.geometry("{}x{}+{}+{}".format(window_width,
                                               window_height, x_cordinate, y_cordinate))
    Label(login_screen, text="Please enter details below to login", bg="#977EF2", width="300",
          height="2", font=("Calibri", 15)).pack()
    Label(login_screen, text="", bg="#87ceeb").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ", bg="#F25C05", width=15,
          height=1, font=("Calibri", 13)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="", bg="#87ceeb").pack()
    Label(login_screen, text="Password * ", bg="#F25C05", width=15,
          height=1, font=("Calibri", 13)).pack()
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="", bg="#87ceeb").pack()
    Label(login_screen, text="", bg="#87ceeb").pack()
    Button(login_screen, text="Login", width=15,
           height=2, command=login_verify, highlightbackground="#F25C05", font=("Calibri", 13)).pack()

    Label(login_screen, text="", bg="#87ceeb").pack()
    Label(login_screen, text="User Not Found",
          fg="red", font=("calibri", 14)).pack()

# Deleting popups


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.configure(bg="#87ceeb")
    main_screen.title("Account Login")
    main_screen.resizable(False, False)
    window_height = 450
    window_width = 450
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2)-150)
    main_screen.geometry("{}x{}+{}+{}".format(window_width,
                                              window_height, x_cordinate, y_cordinate))
    Label(text="Select Your Choice", bg="#977EF2", width="300",
          height="2", font=("Calibri", 15)).pack()
    Label(text="", bg="#87ceeb").pack()
    Label(text="", bg="#87ceeb").pack()
    Label(text="", bg="#87ceeb").pack()
    Button(text="Login", height="2", width="25",
           command=login, highlightbackground="#F25C05", font=("Calibri", 13)).pack()
    Label(text="", bg="#87ceeb").pack()
    Label(text="", bg="#87ceeb").pack()
    Button(text="Sign Up", height="2", width="25",
           command=signup, highlightbackground="#F25C05", font=("Calibri", 13)).pack()

    main_screen.mainloop()


main_account_screen()
