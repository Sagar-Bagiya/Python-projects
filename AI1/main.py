import winsound

import pyttsx3
import speech_recognition as sr
import datetime
import os
import pywhatkit as kit
quary = " "

def speak(input):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    engine.say(input)
    engine.runAndWait()

def takecommand():
    global quary
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.energy_threshold = 870
        r.pause_threshold = 1

        audio = r.listen(source, timeout=None, phrase_time_limit=None)
    try:
        print("recognize....")
        quary = r.recognize_google(audio)
        print(f"you say: {quary}")

    except Exception as e:
        return "None"

    # except sr.UnknownValueError:
    #     print("Could not understand audio")
    #     takecommand()
    #
    # except sr.RequestError as e:
    #     print("Could not request results; {0}".format(e))
    #     return "sir please conect me to internet"

    return quary

def wish_me():
    intro = "i am jarvis, how can i help you"
    hour = int (datetime.datetime.now().hour)
    if hour > 6 and hour < 12:
        quary = "Good morning sir"
    elif hour >= 12 and hour < 18:
        quary = "Good afternoon sir"
    else:
        quary = "Good evening sir"
    speak(quary)
    speak(intro)

def read_data(quary):
    with open("my file.txt", "r") as f:
        data = f.readlines()
        mod = False
        for line in data:
            if mod is True:
                line = line.replace("\n", "")
                return line
            if quary in line:
                mod = True

def write_data(question, answer):
    with open("my file.txt", "a") as f:
        f.write("\n")
        f.write(question)
        f.write("\n")
        f.write(answer)


wish_me()

while True:
    quary = takecommand().lower()
    if True:
        mystr = quary
        if "open notepad" in quary:
            speak("yes sir")
            speak("ok sir, i am opening notepad, please wait some time, i'm trying my best")
            npath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(npath)
            speak("your notepad is open!")
            winsound.MessageBeep()

        elif "open chrome" in quary:
            speak("yes sir")
            speak("ok sir, i am opening chrome, please wait some time, i'm trying my best")
            npath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)
            speak("your google chrome is open!")
            winsound.MessageBeep()

        elif "open youtube" in quary:
            speak("yes sir")
            speak("sir,what should i search on youtube")
            cm = takecommand().lower()
            kit.playonyt(cm)

        elif ("according to wikipedia" or "in wikipedia") in quary:
            speak("yes sir")
            cm = quary
            cm = cm.replace("according to wikipedia", "?")
            cm = cm.replace("in wikipedia", "?")
            data = kit.info(topic=cm, lines=2, return_value=True)
            speak("according to wikipedia," + data)

        elif "open google" in quary:
            speak("yes sir")
            speak("sir what should i search on google")
            cm = takecommand()
            cm = cm.lower()
            kit.search(cm)

        elif "what is" in quary:
            speak("yes sir")
            answer = read_data(quary)
            speak(answer)

        elif "+" in mystr:
            speak("yes sir")
            list = mystr.split(" ")
            ref = list.index("+")
            num1 = float(list[ref - 1])
            num2 = float(list[ref + 1])
            operation = str(num1 + num2)
            speak(quary)
            speak(operation)
        elif "-" in mystr:
            speak("yes sir")
            list = mystr.split(" ")
            ref = list.index("-")
            num1 = float(list[ref - 1])
            num2 = float(list[ref + 1])
            operation = str(num1 - num2)
            quary = quary.replace("-", "minus")
            speak(quary)
            speak(operation)

        elif "x" in mystr.lower():
            speak("yes sir")
            mystr = mystr.lower()
            list = mystr.split(" ")
            ref = list.index("x")
            num1 = float(list[ref - 1])
            num2 = float(list[ref + 1])
            operation = str(num1 * num2)
            speak(quary.replace("x", "multiply by"))
            speak(operation)

        elif "/" in mystr:
            speak("yes sir")
            list = mystr.split(" ")
            ref = list.index("/")
            num1 = float(list[ref - 1])
            num2 = float(list[ref + 1])
            operation = str(num1 / num2)
            quary = quary.replace("/", "divide by")
            speak(quary)
            speak(operation)

        elif "shutdown" in quary:
            speak("ok sir,i enjoyed talking with you!, have a good day!")
            break



