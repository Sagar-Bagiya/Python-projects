from time import sleep
import cv2
import numpy as np
import pyautogui
import pytesseract

# run = True

def getPosition(imgList, myword, draw = False):
    for i, img in enumerate(imgList) : 
            results = pytesseract.image_to_data(img)
            for result in results.splitlines() :
                result = result.split()
                if len(result)==12:
                    # print(result[11])
                    if str(result[11]).lower() == myword.lower():
                        x,y,w,h = int(result[6]),int(result[7]),int(result[8]),int(result[9])
                        cx,cy = x+w//2, y+h//2
                        # print(result)
                        if draw:
                            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)
                            cv2.circle(img, (cx,cy), 10, (255,0,0), -1)
                            # cv2.imshow('output', img)
                        # print(f"skip is found in list-{i}")
                        return i, cx, cy
    return  0, 0, 0

def centerPoint(centerPoint, imgSize, displaySize):
    mx, my = 0, 0
    mx = int(np.interp(centerPoint[0], imgSize[1], displaySize[0]))
    my = int(np.interp(centerPoint[1], imgSize[0], displaySize[1]))
    # print(mx, my)
    # 960 540
    return mx, my

def disText_command(inputW, timeout = 0):
    runCount = 0
    while True :
        pytesseract.pytesseract.tesseract_cmd = r'D:\teserect\tesseract.exe'
        img = pyautogui.screenshot()
        gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
        # gray = cv2.imread(r'D:\python project\AI2\test\screenshot\Screenshot(3).JPEG',0)
        # # image procesing
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret_, thresimg = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
        # thresimg = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 1)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # img = cv2.resize(img, (400,400))
        # print(img.shape)

        y,x = gray.shape

        img1 = thresimg[0:int(y/2),0:int(x/2)]
        img2 = thresimg[0:int(y/2),int(x/2):x]
        img3 = thresimg[int(y/2):y,0:int(x/2)]
        img4 = thresimg[int(y/2):y,int(x/2):x]

        imgList = [img1, img2, img3, img4]
        imgSizeList = [[(0, img.shape[0]),(0, img.shape[1])] for img in imgList]

        # disX,disY = 1282, 722
        # disX,disY = 1920 1080
        disX,disY = pyautogui.size()
        displaySizeList = [((0, disX/2),(0, disY/2)),((disX/2, disX),(0, disY/2)),((0, disX/2),(disY/2, disY)),((disX/2, disX),(disY/2, disY))]

        imgIndex,cx,cy = getPosition(imgList, inputW, draw= True)

        if cx and cy is not False:
            mx, my = centerPoint((cx, cy), imgSize=imgSizeList[imgIndex], displaySize= displaySizeList[imgIndex])
            print(mx, my)
            pyautogui.click(mx, my)
            sleep(0.2)
            return True
            
        elif runCount >= timeout :
            return False

        else :
            # print(runCount)
            runCount += 1
            # global run
            # run = False
            
        

# while run:
#     sleep(0.5)
#     print("Loading...")
#     main("code")

# print("..Done..")     