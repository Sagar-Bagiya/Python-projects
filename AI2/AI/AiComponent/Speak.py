import pyttsx3

engine = pyttsx3.init()
def speak(input,voice=0,rate=174):
    try:
        voices = engine.getProperty("voices")
        engine.setProperty('voice', voices[voice].id)
        engine.setProperty('rate', rate)
        engine.say(input)
        engine.runAndWait()
    except Exception as e:
        print(e)    


