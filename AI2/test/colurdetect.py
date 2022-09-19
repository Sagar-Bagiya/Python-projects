import cv2
import numpy as np

L_limit=np.array([98,50,50]) # setting the blue lower limit
U_limit=np.array([139,255,255]) # setting the blue upper limit
 
# [139,255,255], [98,50,50]  # for blue
# [180, 255, 255], [159, 50, 70] #for red

# color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
#               'white': [[180, 18, 255], [0, 0, 231]],
#               'red1': [[180, 255, 255], [159, 50, 70]],
#               'red2': [[9, 255, 255], [0, 50, 70]],
#               'green': [[89, 255, 255], [36, 50, 70]],
#               'blue': [[128, 255, 255], [90, 50, 70]],
#               'yellow': [[35, 255, 255], [25, 50, 70]],
#               'purple': [[158, 255, 255], [129, 50, 70]],
#               'orange': [[24, 255, 255], [10, 50, 70]],
#               'gray': [[180, 18, 230], [0, 0, 40]]}

img = cv2.imread(r"D:\python project\AI2\test\resorce\shape.jpg")

def colurDetect(frame):

	into_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	b_mask=cv2.inRange(into_hsv,L_limit,U_limit)

	blue=cv2.bitwise_and(frame,frame,mask=b_mask)
	# this will give the color to mask.
    
	cv2.imshow('Original',frame) # to display the original frame
	cv2.imshow('mask',b_mask) # to display the original frame
	cv2.imshow('Blue Detector',blue) # to display the blue object output

	cv2.waitKey(0)

colurDetect(img)

