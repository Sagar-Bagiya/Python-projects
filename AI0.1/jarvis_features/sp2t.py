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

def takecommand():
    global quary
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=5)
    try:
        quary = r.recognize_google(audio)
        print(f"you say: {quary}")

    except sr.UnknownValueError:
        print("Could not understand audio")
        takecommand()

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return "sir please conect me to internet"

    return quary

if __name__ == "__main__":
    print(speech2text())