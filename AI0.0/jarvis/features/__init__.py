import jarvis.features._wikipedia
import jarvis.features.date_time
import jarvis.features.launch_app

class feature:
    def __init__(self):
        pass
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

print("i am in feature")