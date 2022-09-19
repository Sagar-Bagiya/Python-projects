import cv2 as cv
import numpy as np


img = cv.imread("finger-1.jpg")

if img is None:
    sys.exit("could not founnd image.")


cv.imshow("my window", img)
k = cv.waitKey(0)

if k == ord('s'):
    cv.imwrite('save image.png', img)



