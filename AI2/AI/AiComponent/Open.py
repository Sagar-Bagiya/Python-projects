import os
import winsound
try:
    import pywhatkit as kit
except Exception as e:
    print("Error in /Open modual is: ",e)
    

def localApp(appPath):
    try:
        os.startfile(appPath)
        winsound.MessageBeep()
    except Exception as e:
        print(e)
        
def youtube(takecommand):
    try:
        cm = takecommand().lower()
        kit.playonyt(cm)
    except Exception as e:
        print(e)

def wikipedia(quary):
    try:
        cm = quary
        cm = cm.replace("according to wikipedia", "?")
        cm = cm.replace("in wikipedia", "?")
        data = kit.info(topic=cm, lines=2, return_value=True)
        return data  
    except Exception as e:
        print(e)

def google(cm):
    try:
        cm = cm.lower()
        kit.search(cm)
    except Exception as e:
        print(e)
