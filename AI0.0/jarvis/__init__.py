import jarvis.features
import jarvis.function
work = jarvis.features.feature()
fun = jarvis.function.fumctions()
class Assistant:
    def __init__(self):
        pass

    def listen(self):
        try:
            result = fun.speech2text()
        except Exception as e:
            print(e)
            return None
        return result

    def speak(self, text):
        try:
            result = fun.text2speech(text)
        except Exception as e:
            print(e)
            return None
        return result

    def tell_me_date(self):
        try:
            result = work.date_is()
        except Exception as e:
            print(e)
            return None
        return result

    def tell_me_time(self):
        try:
            result = work.time_is()
        except Exception as e:
            print(e)
            return None
        return result

    def Wikipedia(self, topic):
        try:
            result = work._wikipedia(topic)
        except Exception as e:
            print(e)
            return None
        return result

    def open_app(self, path):
        try:
            result = work.launch_app(path)
        except Exception as e:
            print(e)
            return None
        return result

print("i am in jarvis")

if __name__ == "__main__":
    jarvis = Assistant()
    # print(jarvis.tell_me_date())
    # print(jarvis.tell_me_time())
    # jarvis.open_app("C:\\Program Files (x86)\\Notepad++\\notepad++.exe")
    # jarvis.speak("hello boss")
    jarvis.speak(jarvis.listen())