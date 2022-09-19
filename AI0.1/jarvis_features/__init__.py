import jarvis_features.sp2t
import jarvis_features.t2sp
import jarvis_features._wikipedia
import jarvis_features.date_time
import jarvis_features.launch_app
import jarvis_features.quary
import jarvis_features.jarvis_txt
import jarvis_features.keyboard_fun

yt = keyboard_fun.ytf()

class features:
    def __init__(self):
        pass
    def read_data(self, quary):
        try:
            result = jarvis_txt.read_data(quary)
        except Exception as e:
            print(e)
            return None
        return result

    def write_data(self, question, answer):
        try:
            result = jarvis_txt.write_data(question, answer)
        except Exception as e:
            print(e)
            return None
        return result

    def question_in_db(self,question):
        try:
            result = quary.jarvis_dict(question)
        except Exception as e:
            print(e)
            return None
        return result

    def speak(self, text):
        try:
            result = t2sp.text2speech(text)
        except Exception as e:
            print(e)
            return None
        return result

    def listen(self):
        try:
            result = sp2t.speech2text()
        except Exception as e:
            print(e)
            return None
        return result

    def _wikipedia(self, topic):
        try:
            result = _wikipedia.tell_me_about(topic)
        except Exception as e:
            print(e)
            return None
        return result

    def date_is(self):
        try:
            result = date_time.date()
        except Exception as e:
            print(e)
            return None
        return result

    def time_is(self):
        try:
            result = date_time.time()
        except Exception as e:
            print(e)
            return None
        return result

    def launch_app(self, path):
        try:
            result = launch_app.launch(path)
        except Exception as e:
            print(e)
            return None
        return result

    def close_app(self):
        try:
            result = keyboard_fun.close_current_task()
        except Exception as e:
            print(e)
            return None
        return result

    def yt_play_pause(self):
        try:

            result = yt.Pause_Play()
        except Exception as e:
            print(e)
            return None
        return result

    def yt_mute_unmute(self):
        try:

            result = yt.Mute_unmute()
        except Exception as e:
            print(e)
            return None
        return result

    def yt_Seek_backward(self):
        try:

            result = yt.Seek_backward()
        except Exception as e:
            print(e)
            return None
        return result

    def yt_Seek_forward(self):
        try:

            result = yt.Seek_forward()
        except Exception as e:
            print(e)
            return None
        return result

    def yt_Speed_up(self):
        try:

            result = yt.Speed_up()
        except Exception as e:
            print(e)
            return None
        return result

    def yt_Speed_down(self):
        try:

            result = yt.Speed_down()
        except Exception as e:
            print(e)
            return None
        return result

    def yt_volum_up(self):
        try:

            result = yt.volum_up()
        except Exception as e:
            print(e)
            return None
        return result

    def yt_volum_down(self):
        try:

            result = yt.volum_down()
        except Exception as e:
            print(e)
            return None
        return result
    def yt_full_screen(self):
        try:
            result = yt.full_screen()
        except Exception as e:
            print(e)
            return None
        return result
    def yt_skip_ads(self):
        try:
            result = yt.skip_ads()
        except Exception as e:
            print(e)
            return None
        return result

    def yt_search(self):
        try:
            result = yt.search()
        except Exception as e:
            print(e)
            return None
        return result

    def typing(self, cm):
        try:
            result = keyboard_fun.typing(cm)
        except Exception as e:
            print(e)
            return None
        return result

    def virtual_mouse(self):
        try:
            result = keyboard_fun.virtual_mouse()
        except Exception as e:
            print(e)
            return None
        return result


# print("i am in feature")
if __name__ == "__main__":
    jarvis = features()
    # jarvis.question("what is your name ?")
