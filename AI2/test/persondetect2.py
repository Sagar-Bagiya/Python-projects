import cv2
import face_recognition as fr
import os
import numpy as np

# Load a sample picture and learn how to recognize it.
encoded_imgs = []
name_of_imgs = []
path = 'D:/python project/AI2/test/faceimgs'
for imgName in os.listdir(path) :

    img_name, imgType = os.path.splitext(imgName)

    if imgType == '.jpg' or imgType == '.png':
        imgPath = path + f'/{imgName}'
        img = fr.load_image_file(imgPath)
        face_locations = fr.face_locations(img)
        
        if face_locations :
            encoded_img = fr.face_encodings(img, face_locations)[0]
            encoded_imgs.append(encoded_img)
            name_of_imgs.append(img_name)
# ------------------------------

# cap = cv2.VideoCapture(r'D:\python project\AI2\test\vedio\workout.mp4')
cap = cv2.VideoCapture(0)
# cap.set(3,)
# cap.set(4,)
runing = True

while runing:
    ret, frame = cap.read()
    mainImg = cv2.resize(frame, (400, 400))
    rgb_img = cv2.cvtColor(mainImg, cv2.COLOR_BGR2RGB)

    face_locations = fr.face_locations(rgb_img)
    
    if face_locations : 
        face_encodings = fr.face_encodings(rgb_img, face_locations)
        for face_encoding in face_encodings :
            matches = fr.compare_faces(encoded_imgs, face_encoding)
            name = "Unknown"

            face_distances = fr.face_distance(encoded_imgs, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = name_of_imgs[best_match_index]
                print(name)
            # face_names.append(name)

    cv2.imshow('out', mainImg)
    cv2.waitKey(1)
    
cap.release()