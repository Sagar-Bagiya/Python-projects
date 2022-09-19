import random

import jarvis
jarvis = jarvis.Assistant()


GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there","service","ok service"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

def main(command):
    if "open notepad" in command:
        jarvis.open_app("C:\\Program Files (x86)\\Notepad++\\notepad++.exe")
        jarvis.speak("sir, your notepad is ready to use!")
    if "open mozilla" in command:
        jarvis.open_app("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        jarvis.speak("boss, your mozila is hear")
    if "open youtube" in command:
        jarvis.speak("i am not found youtube ,sir")
    if "date" in command:
        jarvis.speak(jarvis.tell_me_date())
    if "time" in command:
        jarvis.speak(jarvis.tell_me_time())
    if "wikipedia" in command:
        jarvis.speak(jarvis.Wikipedia(topic))
if True:
    lock = jarvis.listen()
    if lock in GREETINGS:
        jarvis.speak(random.choice(GREETINGS_RES))
        command = jarvis.listen()
        jarvis.speak("sir, please wait few second!,i will try my best!")
        main(command)
        # if "goodby" in command:
        #     jarvis.speak("I am always eager to talk to you!,Just say Alexa to wake me up!, have a good day!")
        #     break