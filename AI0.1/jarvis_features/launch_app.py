import os

def launch(path_of_app):
    try:
        os.startfile(path_of_app)
        return True
    except Exception as e:
        print(e)
        return False
