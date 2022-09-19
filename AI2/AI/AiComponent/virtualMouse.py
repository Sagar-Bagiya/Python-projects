import time
import cv2
import numpy
from cvzone import HandTrackingModule as ht
import pyautogui

def virtual_mouse():
    try:
        wscr, hscr = pyautogui.size()
        wcam, hcam = 640, 480
        pTime = 0
        frameR = 200
        ofsetY = 55
        smoothening = 12
        plocX, plocY = 0, 0
        clocX, clocY = 0, 0

        cap = cv2.VideoCapture(0)
        cap.set(3, wcam)
        cap.set(4, hcam)

        detector = ht.HandDetector(maxHands=1)

        while True:
            
            sucss, img = cap.read()
            hands, img = detector.findHands(img)

            if hands:
                hand1 = hands[0]
                lmlist = hand1["lmList"]

                if lmlist!=0:
                    # print(lmlist)
                    x1, y1 = lmlist[8]
                    # x2, y2 = lmlist[12]
                    # print(x1, y1)

                    cv2.rectangle(img, (frameR, frameR), (wcam - frameR, hcam - frameR + ofsetY), (255, 0, 255), 2)

                    fingers = detector.fingersUp(hand1)
                    # print(fingers)

                    if fingers[1] == 1 :
                        x3 = numpy.interp(x1, (frameR, wcam-frameR), (0, wscr))
                        y3 = numpy.interp(y1, (frameR, hcam-frameR+ofsetY), (0, hscr))

                        clocX = plocX + (x3-plocX) /smoothening
                        clocY = plocY+ (y3-plocY) /smoothening
                        # print(clocX,clocY)

                        pyautogui.moveTo(wscr-clocX, clocY)
                        cv2.circle(img, (x1, y1), 15, (0, 0, 255), cv2.FILLED)
                        plocX, plocY= clocX, clocY

                    if fingers[1:] == [1,1,0,0] :
                        length, lineinfo, img = detector.findDistance(lmlist[8], lmlist[12], img)
                        print(length)

                        if length<40:
                            cv2.circle(img, (lineinfo[4], lineinfo[5]), 15, (0, 255, 0), cv2.FILLED)
                            pyautogui.click()
                            time.sleep(0.1)

            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime

            cv2.putText(img,str(int(fps)), (20,50), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,255), 3)
            cv2.imshow("my image", img)
            key = cv2.waitKey(1)
            if key != -1:
                break

    except Exception as e:
        print(e)
        return False

# x,y = pyautogui.size()
# print(x,y)
# pyautogui.moveTo(x,y)
# virtual_mouse()