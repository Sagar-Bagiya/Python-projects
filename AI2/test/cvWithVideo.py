import cv2
from cvzone import HandTrackingModule

detector = HandTrackingModule.HandDetector()

cap = cv2.VideoCapture(r'D:\python project\AI2\test\vedio\workout3.mp4')

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (900,700))
    detector.findHands(frame)
    cv2.imshow('out',frame)
    key = cv2.waitKey(20)
    if key == 97 :
        break
    
cap.release()
cv2.destroyAllWindows()