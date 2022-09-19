import numpy as np
import cv2

mainImg = np.zeros((400,500,3),np.uint8)
hscr,wscr,size = mainImg.shape
# mainImg[:] = (255, 0 ,0)
# print(h,w,size)
cx, cy = wscr//2, hscr//2
cv2.line(mainImg, (0, cy), (wscr, cy), (255,0,255), 3)
cv2.line(mainImg, (cx, 0), (cx, hscr), (255,0,255), 3)
cv2.putText(mainImg,("X axis"), (cx+10, cy+15), cv2.FONT_HERSHEY_COMPLEX,.7,(0,0,255), 1)
cv2.putText(mainImg,("y axis"), (cx+5, 10), cv2.FONT_HERSHEY_COMPLEX,.7,(0,0,255), 1)

for j in range(3):
    copyimg = mainImg.copy()
    csize = 1
    for i in range(0,wscr,10):
        cv2.circle(copyimg, (0 + i,cy), csize, (100,255,100), -1)
        csize+=1
        cv2.imshow('img', copyimg)
        if i is not wscr:
            cv2.waitKey(200)
