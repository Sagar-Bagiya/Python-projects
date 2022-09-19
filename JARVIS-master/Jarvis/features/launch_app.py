import os

def launch_app(path_of_app):
    try:
        os.startfile(path_of_app)
        return True
    except Exception as e:
        print(e)
        return False
