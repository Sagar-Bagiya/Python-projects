import numpy as np
import cv2
import pyautogui
   
  
# take screenshot using pyautogui
image = pyautogui.screenshot()
   
image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
   

# writing it to the disk using opencv
# cv2.imshow('scrsh', image)
# cv2.imwrite("image1.png", image)
# cv2.waitKey(0)

print(image.shape)
# print(pyautogui.size())