import datetime
import random
from jarvis_features import features
import time
import pywhatkit as kit
# from pynput.mouse import Button, Controller
# mouse = Controller
jarvis = features()

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
    jarvis.speak(quary)
    jarvis.speak(intro)

GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there","service","ok service"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

# wish_me()

while True:

    cm = jarvis.listen()

    if "open youtube" in cm:
        jarvis.speak("yes sir")
        jarvis.speak("sir,what should i search on youtube")
        cm = jarvis.listen()
        kit.playonyt(cm)
        while True:
            cm = jarvis.listen()
            if "keep ad" in cm or "skip ad" in cm or "ad" in cm:
                jarvis.yt_skip_ads()
            if "full screen" in cm:
                jarvis.yt_full_screen()
            if "play" in cm or "band kar" in cm or "pause" in cm or "chalu kar" in cm:
                jarvis.yt_play_pause()
            if "volume up" in cm:
                jarvis.yt_volum_up()
            if "volume down" in cm:
                jarvis.yt_volum_down()
            if "forward" in cm:
                jarvis.yt_Seek_forward()
            if "backward" in cm or "back" in cm:
                jarvis.yt_Seek_backward()
            if "mute" in cm or "unmute" in cm:
                jarvis.yt_mute_unmute()
            if "speed up" in cm:
                jarvis.yt_Speed_up()
            if "speed down" in cm:
                jarvis.yt_Speed_down()
            if "close" in cm:
                jarvis.close_app()
                break
            if "search" in cm:
                jarvis.yt_search()
                jarvis.speak("yes boss, what you want to search?")
                cm = jarvis.listen()
                jarvis.typing(cm)

    elif "close it" in cm:
        jarvis.close_app()

    elif "virtual mouse mode" in cm:
        jarvis.speak("ok sir, i am activating virtual mouse mode!")
        jarvis.virtual_mouse()

    elif "ok good by" in cm:
        jarvis.speak("good by  sir!, have a good day!")
        break

    elif jarvis.read_data(cm):
        jarvis.speak(jarvis.read_data(cm))