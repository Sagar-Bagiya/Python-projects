import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 174)


def text2speech(text):
    """
     Convert any text to speech
     :param text: text(String)
     :return: True/False (Play sound if True otherwise write exception to log and return  False)
     """

    try:
        engine.say(text)
        engine.runAndWait()
        return True
    except:
        t = "Sorry I couldn't understand and handle this input"
        print(t)
        return False


if __name__ == "__main__":
    text2speech("hello sir, how may i help you , this is test program")
