import numpy as np
import cv2

img = cv2.imread(r'D:\python project\AI2\test\resorce\apple.jpg')
# myarr = np.zeros((400,400,3),np.uint8)
# myarr[:] = (0,0,0)
# print(myarr)
img = cv2.resize(img, (400,500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3),cv2.BORDER_DEFAULT)
cany = cv2.Canny(blur, 5, 200)
dialet = cv2.dilate(cany,(5,5))
contours, hierarchy = cv2.findContours(dialet, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# print(contours)
cv2.drawContours(img, contours, -1, (255, 0, 255), 1)
cv2.drawContours(img, contours, -1, (255, 0, 255), 1)

# cv2.imshow("output",gray)
# cv2.imshow("output2",cany)
cv2.imshow("output3",dialet)
cv2.imshow("output4",img)

cv2.waitKey(0)