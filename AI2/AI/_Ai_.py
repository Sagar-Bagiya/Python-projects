from .AiComponent import *

class myAi:

    def __init__(self, **kwargs):
        self._voice = kwargs.get('voice',0)
        self._sprate = kwargs.get('sprate',174)

    def disText_command(self, user_command, timeout):
        return displayTextCommand.disText_command(user_command, timeout)

    def Query_analysis (self,input):
       return Query_analysis.Query_analysis(input)

    def query_check(self, user_command):
        query_info = self.Query_analysis(user_command)
        # print(query_info)

        if query_info[2] == "command":
            actions = query_info[0]
            subjects = query_info[1]
            query = ""
            for action in actions:
                for subject in subjects:
                    query += f"{action} {subject} "
            return query

        elif query_info[2] == "Interrogative":
            if ' jarvis' in user_command:
                return 'i giv you Interrogative ans'
            else :
                return False

        elif query_info[2] == "udagar":
            return 'i give you udagar ans'

        else : return query_info

    def listen(self):
        return Listen.listen()

    def speak(self,input,voice=0,rate=174):
        Speak.speak(input,
        voice=(self._voice) if voice==0 else voice,
        rate=(self._sprate) if rate==174 else rate)

    def wish_me(self):
        wish,intro=Wish.wish_me()
        self.speak(wish)
        self.speak(intro)

    def virtual_mouse(self):
        virtualMouse.virtual_mouse()

    class math:
        def add(mystr):return Math.add(mystr)
        def sub(mystr):return Math.sub(mystr)
        def mul(mystr):return Math.mul(mystr)
        def div(mystr):return Math.division(mystr)

    class open:
        def localApp(appPath): Open.localApp(appPath)
        def notepad(): Open.localApp(App_path.notepad)
        def chrome(): Open.localApp(App_path.chrome)
        def mozilla(): Open.localApp(App_path.mozilla)
        def youtube(mystr): Open.youtube(mystr)
        def google(mystr): Open.google(mystr)
        def wikipedia(mystr): return Open.wikipedia(mystr)

    class crud:
        def read(): return Crud.read_data()
        def write(question, answer): Crud.write_data(question, answer)

    class Datetime:
        def tell_me_date():date_time.date()
        def tell_me_time():date_time.time()

    class keyBoard:
        def close_current_task():keyboard_function.close_current_task()
        def type(mystr):keyboard_function.type(mystr)
        class ytAuto(keyboard_function.ytAuto):
            pass

