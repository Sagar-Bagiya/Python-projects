import keyboard


def close_current_task():
    try:
        keyboard.press_and_release('alt+f4')
        return True
    except Exception as e:
        print(e)
        return False

def type(cm):
    try:
        keyboard.write(cm)
        keyboard.press_and_release('enter')
        return True
    except Exception as e:
        print(e)
        return False


class ytAuto:
    def __init__(self):
        pass
    
    # def skip_ads(self):
    #     try:
    #         # mouse.position = (1825, 920) for full screen
    #         mouse.position = (1100, 650)
    #         mouse.click(Button.left, 1)
    #         return True
    #     except Exception as e:
    #         print(e)
    #         return False

    def search():
        try:
            keyboard.press_and_release('/')
            return True
        except Exception as e:
            print(e)
            return False

    def full_screen():
        try:
            keyboard.press_and_release('f')
            return True
        except Exception as e:
            print(e)
            return False

    def Pause_Play():
        try:
            keyboard.press_and_release('k')
            return True
        except Exception as e:
            print(e)
            return False

    def Mute_unmute():
        try:
            keyboard.press_and_release('m')
            return True
        except Exception as e:
            print(e)
            return False

    def Seek_backward():
        try:
            keyboard.press_and_release('j')
            return True
        except Exception as e:
            print(e)

    def Seek_forward():
        try:
            keyboard.press_and_release('l')
            return True
        except Exception as e:
            print(e)
            return False

    def Speed_up():
        try:
            keyboard.press_and_release('shift+>')
            return True
        except Exception as e:
            print(e)
            return False

    def Speed_down():
        try:
            keyboard.press_and_release('shift+<')
            return True
        except Exception as e:
            print(e)
            return False

    def volum_down():
        try:
            keyboard.press_and_release('down')
            return True
        except Exception as e:
            print(e)
            return False

    def volum_up():
        try:
            keyboard.press_and_release('up')
            return True
        except Exception as e:
            print(e)
            return False


# if __name__ == "__main__":
#     virtual_mouse()


# yt = ytf()
# time.sleep(3)
# yt.skip_ads()