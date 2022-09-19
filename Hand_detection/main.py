import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2, detectionCon=0.7)

ans = "length:0"
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
        print(type1, " hand",  finger1)

        if len(hands)==2:
            hand2 = hands[1]
            lmlist2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            center2 = hand2["center"]
            type2 = hand2["type"]
            length, info, img = detector.findDistance(lmlist1[8], lmlist2[8], img)
            ans = "length:" + str(int(length))
            finger2 = detector.fingersUp(hand2)
            print(type2, " hand", finger2)

    img = cv2.putText(img, ans, (50, 50), cv2.FONT_ITALIC, 1, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.imshow("Image", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

