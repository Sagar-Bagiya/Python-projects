
def read_data(quary):
    with open("my file.txt", "r") as f:
        data = f.readlines()
        mod = False
        for line in data:
            if mod is True:
                line = line.replace("\n", "")
                return line
            if quary in line:
                mod = True
def write_data(question, answer):
    with open("my file.txt", "a") as f:
        f.write("\n")
        f.write(question)
        f.write("\n")
        f.write(answer)
def speak(input):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    engine.say(input)
    engine.runAndWait()
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
        speak("sorry sir i can't understand, please say again")
        takecommand()

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return "sir please conect me to internet"

    return quary
def wish_me():
    intro = "i am jarvis, how can i help you"
    hour = int (datetime.datetime.now().hour)
    if hour > 6 and hour < 12:
        quary = "Good morning sir"
    elif hour > 12 and hour < 18:
        quary = "Good afternoon sir"
    else:
        quary = "Good evening sir"
    speak(quary)
    speak(intro)


# write_data("what is your name", "my name is jarvis")
# write_data("what is my name", "sagar")
# print(read_data("your name"))

def mathamatics(mystr):
    if "+" in mystr:
        list = mystr.split(" ")
        ref = list.index("+")
        num1 = float(list[ref - 1])
        num2 = float(list[ref + 1])
        operation = num1 + num2
        return str(operation)
    elif "-" in mystr:
        list = mystr.split(" ")
        ref = list.index("-")
        num1 = float(list[ref - 1])
        num2 = float(list[ref + 1])
        operation = num1 - num2
        return str(operation)

    elif "*" in mystr:
        list = mystr.split(" ")
        ref = list.index("*")
        num1 = float(list[ref - 1])
        num2 = float(list[ref + 1])
        operation = num1 * num2
        return str(operation)

    elif "/" in mystr:
        list = mystr.split(" ")
        ref = list.index("/")
        num1 = float(list[ref - 1])
        num2 = float(list[ref + 1])
        operation = num1 / num2
        return str(operation)


class mathamatic:

    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2
    def add(self):
        return str(self.num1 + self.num2)
    def sub(self):
        return str(self.num1 - self.num2)
    def multiplication(self):
        return str(self.num1 * self.num2)
    def division(self):
        return str(self.num1 / self.num2)


detector = mathamatic(num1, num2)
list = mystr.split(" ")
ref = list.index("+")
