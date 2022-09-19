import pyttsx3
import os
import winsound
import random
import datetime
import speech_recognition as sr

def speech2text():
    """
    Fetch input from mic
    return: user's voice input as text if true, false if fail
    """
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            # r.adjust_for_ambient_noise(source, duration=1)
            r.energy_threshold = 4000
            r.pause_threshold = 0.8
            audio = r.listen(source, phrase_time_limit=5)

        try:
            print("Recognizing...")
            command = r.recognize_google(audio_data=audio, language='en-in').lower()
            print(f'You said: {command}')
        except:
            print('Please try again')
            command = speech2text()
        return command
    except Exception as e:
        print(e)
        return False

def text2speech(text):
    """
     Convert any text to speech
     :param text: text(String)
     :return: True/False (Play sound if True otherwise write exception to log and return  False)
     """
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    try:
        engine.say(text)
        engine.runAndWait()
        return True
    except:
        t = "Sorry I couldn't understand and handle this input"
        print(t)
        return False

def wish_me():
    quary = " "
    intro = "i am jarvis, how can i help you"
    hour = int (datetime.datetime.now().hour)
    if hour > 6 and hour < 12:
        quary = "Good morning sir"
    elif hour >= 12 and hour < 18:
        quary = "Good afternoon sir"
    else:
        quary = "Good evening sir"
    text2speech(quary)

def read_data(quary):
    with open("QandAns.txt", "r") as f:
        data = f.readlines()
        mod = False
        for line in data:
            if mod is True:
                line = line.replace("\n", "")
                return line
            else:
                if quary in line:
                    mod = True
def read_greetings(quary):
    with open("GREETINGS.txt", "r") as f:
        data = f.readlines()
        for line in data:
            if quary in line:
                return True

def write_data(question, answer):
    with open("QandAns.txt", "a") as f:
        f.write("\n")
        f.write(question)
        f.write("\n")
        f.write(answer)

def main(command):
    if "open notepad" in command:
        os.startfile("C:\\Program Files (x86)\\Notepad++\\notepad++.exe")
        text2speech("sir, your notepad is ready to use!")
    elif "open mozilla" in command:
        os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        text2speech("boss, your mozila is hear")
    elif "open youtube" in command:
        text2speech("i am not found youtube ,sir")
    elif "wikipedia" in command:
        text2speech("ok sir")
    elif "today date" in command:
        d = str(datetime.datetime.today().date().strftime("%d"))
        m = str(datetime.datetime.today().date().strftime("%B"))
        y = str(datetime.datetime.today().date().strftime("%Y"))
        print(d+" "+m+" "+y)
        text2speech("Today date is"+d+","+m+","+y)
    elif "time" in command:
        h = str(datetime.datetime.today().time().strftime("%H"))
        m = str(datetime.datetime.today().time().strftime("%M"))
        s = str(datetime.datetime.today().time().strftime("%S"))
        print(h+" "+m+" "+s)
        text2speech("sir current time is!"+h+"hour!"+m+"minute!,"+s+"seconds!")


    else:
        text2speech(read_data(command))


# GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
#              "ok jarvis", "are you there","service","ok service,hey jarvis are you there"]
# GREETINGS_RES = ["always there for you sir!", "i am ready sir",
#                  "your wish my command", "how can i help you sir?", "i am online and ready sir"]


if __name__ == "__main__":
    wish_me()
    while True:
       greetings = speech2text()

       if read_greetings(greetings):
            # text2speech(GREETINGS_RES[random.randrange(0, 5)])
            text2speech("yes sir!")
            command = speech2text()
            if "talk with me" in command:
                text2speech("ok sir i am activating mod2")
                while True:
                    command = speech2text()
                    if "ok good by" in command:
                        break
                    else:
                        main(command)

            else:
             main(command)





