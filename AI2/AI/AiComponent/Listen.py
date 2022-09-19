import speech_recognition as sr

r = sr.Recognizer()
# r.energy_threshold = 870
r.energy_threshold = 900
# r.pause_threshold = 1
r.pause_threshold = 0.9


def listen():
    # obtain audio from the microphone
    # device_index=1 for wo mic
    try:
        with sr.Microphone(device_index=2) as source:
            print("listening......")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=None, phrase_time_limit=7)
    except Exception as e:
        print(e)

    try:
        print("recognize....")
        responce = r.recognize_google(audio)
        print(f"you say: {responce}")
        
    except Exception as e:
        print(e,"sorry, i could not understand. could you please say that agai.........")
        responce = 'None'

    return str(responce)

        # except sr.UnknownValueError:
        #     print("Could not understand audio")
        #     takecommand()
        #
        # except sr.RequestError as e:
        #     print("Could not request results; {0}".format(e))
        #     return "sir please conect me to internet"

    # select mic with this code
    # for index, name in enumerate(sr.Microphone.list_microphone_names()):
    #     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# if __name__ == "__main__":
    
#     listen()