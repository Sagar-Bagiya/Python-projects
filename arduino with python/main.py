import cv2
from cvzone.HandTrackingModule import HandDetector
import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1,detectionCon=.7)
mod = 0

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand1 = hands[0]
        lmlist1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        center1 = hand1["center"]
        type1 = hand1["type"]
        finger1 = detector.fingersUp(hand1)
        finger = finger1[1]
        length, info, img = detector.findDistance(lmlist1[8], lmlist1[12], img)

        print(type1, " hand", finger, length)


        if (type1== "Right") and (finger == 1) :

            if mod == 0 and length <= 25 :
                board.digital[13].write(1)
                time.sleep(.1)
                mod = 1

            if mod != 0 and length > 25 :
                board.digital[13].write(0)
                mod = 0

    cv2.imshow("Image", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    # x = str(input())
    # if x == "on" :
    #     board.digital[13].write(1)
    # if x == "on" :
    #     board.digital[13].write(0)

