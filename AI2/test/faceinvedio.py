import cv2
from cvzone import PID, FaceDetectionModule, PoseModule

# detector = PoseModule.PoseDetector(detectionCon=.4)
# cap = cv2.VideoCapture(r'D:\python project\AI2\test\vedio\workout3.mp4')

def main():
    cap = cv2.VideoCapture(r'D:\python project\AI2\test\vedio\workout.mp4')
    detector = FaceDetectionModule.FaceDetector()
    # For a 640x480 image center target is 320 and 240
    xPID = PID([1, 0.000000000001, 1], 640 // 2)
    yPID = PID([1, 0.000000000001, 1], 480 // 2, axis=1, limit=[-100, 100])

    while True:
        success, img = cap.read()
        img = cv2.resize(img, (640,480))

        img, bboxs = detector.findFaces(img)
        if bboxs:
            x, y, w, h = bboxs[0]["bbox"]
            cx, cy = bboxs[0]["center"]
            xVal = int(xPID.update(cx))
            yVal = int(yPID.update(cy))

            xPID.draw(img, [cx, cy])
            yPID.draw(img, [cx, cy])

            cv2.putText(img, f'x:{xVal} , y:{yVal} ', (x, y - 100), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


main()
# while True:
#     succ, frame = cap.read()
#     frame = cv2.resize(frame, (500,400))

#     detector.findPose(frame)

#     # data = [{'id': 0, 'bbox': (149, 88, 80, 80), 'score': [0.7131862640380859], 'center': (189, 128)}]
#     # if data:
#     #     x, y, w, h = data[0]['bbox']
#     #     cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
#     cv2.imshow('output', frame)
#     cv2.waitKey(20)