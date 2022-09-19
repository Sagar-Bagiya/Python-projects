import os
import cv2
import face_recognition as fr

encoded_imgs = []
name_of_imgs = []

path = 'D:/python project/AI2/test/faceimgs'
imgsList= os.listdir(path) 

for imgName in imgsList:
    imgPath = path + f'/{imgName}'

    img = fr.load_image_file(imgPath)
    encoded_img = fr.face_encodings(img)[0]

    encoded_imgs.append(encoded_img)
    name_of_imgs.append(os.path.splitext(imgName)[0])
