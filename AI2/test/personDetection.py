import cv2
from cvzone.FaceDetectionModule import FaceDetector
import face_recognition as fr
import os

detector = FaceDetector()
# Load a sample picture and learn how to recognize it.
encoded_imgs = []
name_of_imgs = []
path = 'D:/python project/AI2/test/faceimgs'
for imgName in os.listdir(path) :

    img_name, imgType = os.path.splitext(imgName)

    if imgType == '.jpg' or imgType == '.png':
        imgPath = path + f'/{imgName}'
        img = fr.load_image_file(imgPath)
        encoded_img = fr.face_encodings(img)[0]

        encoded_imgs.append(encoded_img)
        name_of_imgs.append(img_name)

faceids = []
bboxs = []
imgList = []


cap = cv2.VideoCapture(0)
# cap.set(3,)
# cap.set(4,)
runing = True
while runing:
    ret, frame = cap.read()
    mainImg = cv2.resize(frame, (500, 500))
    _, infos = detector.findFaces(mainImg)
    
    for info in infos:
            id, bbox, score, center = info.values()
            x,y,w,h = bbox
            img = mainImg[y-50:y+h,x-30:x+w]

            faceids.append(id)
            bboxs.append(bbox)
            imgList.append(img)

    for img in imgList:
        try :
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face_locations = fr.face_locations(img)
            # print(face_locations)
            face_encodings = fr.face_encodings(img, face_locations)

            for i,data in enumerate(encoded_imgs):
                if(fr.compare_faces(data, face_encodings)[0]):
                    print('Hello ' + name_of_imgs[i])
                    runing = False
                    break
        
        except Exception as e:
            pass

    cv2.imshow('out', mainImg)
    cv2.waitKey(1)
    
