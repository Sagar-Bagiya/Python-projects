from jarvis.function import sp2t
from jarvis.function import t2sp

class fumctions:
    def __init__(self):
        pass

    def text2speech(self, text):
        try:
            result = t2sp.text2speech(text)
        except Exception as e:
            print(e)
            return None
        return result

    def speech2text(self):
        try:
            result = sp2t.speech2text()
        except Exception as e:
            print(e)
            return None
        return result

print("i am in function")
