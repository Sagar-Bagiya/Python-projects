import keyboard
import time
import cv2
import numpy
import autopy
from cvzone import HandTrackingModule as ht
from pynput.mouse import Button, Controller

mouse = Controller()

def close_current_task():
    try:
        keyboard.press_and_release('alt+f4')
        return True
    except Exception as e:
        print(e)
        return False

def typing(cm):
    try:
        keyboard.write(cm)
        keyboard.press_and_release('enter')
        return True
    except Exception as e:
        print(e)
        return False

def virtual_mouse():
    try:
        wscr, hscr = 1280.0, 720.0
        wcam, hcam = 640, 480
        pTime = 0
        frameR = 195
        ofsetY = 55
        smoothening = 9
        plocX, plocY = 0, 0
        clocX, clocY = 0, 0

        cap = cv2.VideoCapture(0)
        cap.set(3, wcam)
        cap.set(4, hcam)

        detector = ht.HandDetector(maxHands=1)

        while True:
            suss, img = cap.read()
            hands, img = detector.findHands(img)

            if hands:
                hand1 = hands[0]
                lmlist = hand1["lmList"]

                if lmlist!=0:
                    # print(lmlist)
                    x1, y1 = lmlist[8]
                    x2, y2 = lmlist[12]
                    # print(x1, y1, x2, y2)

                    cv2.rectangle(img, (frameR, frameR), (wcam - frameR, hcam - frameR + ofsetY), (255, 0, 255), 2)

                    fingers = detector.fingersUp(hand1)
                    # print(fingers)

                    if fingers[1]==1 and fingers[2]==0:
                        x3 = numpy.interp(x1, (frameR, wcam-frameR), (0, wscr))
                        y3 = numpy.interp(y1, (frameR, hcam-frameR+ofsetY), (0, hscr))

                        clocX = plocX + (x3-plocX) /smoothening
                        clocY = plocY+ (y3-plocY) /smoothening
                        # print(clocX,clocY)

                        autopy.mouse.move(wscr-clocX, clocY)
                        cv2.circle(img, (x1, y1), 15, (0, 0, 255), cv2.FILLED)
                        plocX, plocY= clocX, clocY

                    if fingers[1]==1 and fingers[2]==1 and fingers[3]==0 and fingers[4]==0:
                        length, lineinfo, img = detector.findDistance(lmlist[8], lmlist[12], img)
                        # print(length)

                        if length<20:
                            cv2.circle(img, (lineinfo[4], lineinfo[5]), 15, (0, 255, 0), cv2.FILLED)
                            autopy.mouse.click()
                            time.sleep(0.1)

            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime

            cv2.putText(img,str(int(fps)), (20,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)
            cv2.imshow("my image", img)
            cv2.waitKey(1)

    except Exception as e:
        print(e)
        return False


class ytf:
    def __init__(self):
        pass
    def skip_ads(self):
        try:
            # mouse.position = (1825, 920) for full screen
            mouse.position = (1100, 650)
            mouse.click(Button.left, 1)
            return True
        except Exception as e:
            print(e)
            return False

    def search(self):
        try:
            keyboard.press_and_release('/')
            return True
        except Exception as e:
            print(e)
            return False
    def full_screen(self):
        try:
            keyboard.press_and_release('f')
            return True
        except Exception as e:
            print(e)
            return False
    def Pause_Play(self):
        try:
            keyboard.press_and_release('k')
            return True
        except Exception as e:
            print(e)
            return False

    def Mute_unmute(self):
        try:
            keyboard.press_and_release('m')
            return True
        except Exception as e:
            print(e)
            return False

    def Seek_backward(self):
        try:
            keyboard.press_and_release('j')
            return True
        except Exception as e:
            print(e)


    def Seek_forward(self):
        try:
            keyboard.press_and_release('l')
            return True
        except Exception as e:
            print(e)
            return False
    def Speed_up(self):
        try:
            keyboard.press_and_release('shift+>')
            return True
        except Exception as e:
            print(e)
            return False

    def Speed_down(self):
        try:
            keyboard.press_and_release('shift+<')
            return True
        except Exception as e:
            print(e)
            return False
    def volum_down(self):
        try:
            keyboard.press_and_release('down')
            return True
        except Exception as e:
            print(e)
            return False

    def volum_up(self):
        try:
            keyboard.press_and_release('up')
            return True
        except Exception as e:
            print(e)
            return False


if __name__ == "__main__":
    virtual_mouse()


# yt = ytf()
# time.sleep(3)
# yt.skip_ads()