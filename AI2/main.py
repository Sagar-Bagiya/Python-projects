import cv2
import face_recognition as fr

img = fr.load_image_file(r'D:\python project\AI2\test\faceimgs\sagar.jpg')
img = cv2.resize(img, (400,500))
top, right, bottom, left  = fr.face_locations(img)[0]
# cv2.rectangle(img, (left, top), (right, bottom), (0,0,244), 2)
img = img[top:bottom,left:right]
sp = img.shape
print(sp)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imshow('img', img)
cv2.waitKey(0)
