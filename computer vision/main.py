import cv2 as cv
import numpy as np
# ALL ABOUT IMAGE

# Read an image from file (using cv::imread)
# Display an image in an OpenCV window (using cv::imshow)
# Write an image to a file (using cv::imwrite)
#
# img = cv.imread("finger-1.jpg")
#
# if img is None:
#     sys.exit("could not founnd image.")
#
# cv.imshow("my window", img)
# k = cv.waitKey(0)
#
# if k == ord('s'):
#     cv.imwrite('save image.png', img)

#---------------------------------------------------------------------------------


# ALL ABOUT VEDEO
# Learn to read video, display video, and save video.
# Learn to capture video from a camera and display it.
# You will learn these functions : cv.VideoCapture(), cv.VideoWriter()
#---webcam open
# import numpy as np
# import cv2 as cv
# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv.imshow('frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()

#-----both save end file open-----
# cap = cv.VideoCapture('output.mp4')
# if not cap.isOpened():
#     print("we cant open camera")
#     exit()
# save = False
# file = False
# while cap.isOpened():
#     sucess,frame = cap.read()
#
#     if not sucess:
#         print("we can not get frame")
#         break
#     if save == True:
#         if file:
#             fourcc = cv.VideoWriter_fourcc(*'XVID')
#             out = cv.VideoWriter('output2.mp4', fourcc, 20.0, (640, 480))
#
#         frame = cv.flip(frame, 1)
#         out.write(frame)
#     file = False
#
#     cv.imshow("my vedio", frame)
#
#     k = cv.waitKey(30)
#     if k == ord('s'):
#         save = True
#         file = True
#     if k == ord("q"):
#         break
#
# cap.release()
# out.release()
# cv.destroyAllWindows()
#----------------------------------------------------


# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
# # DRAING OPERATION
#     cv.line(frame,(0,0),(600,511),(255,0,0),5)
#     cv.circle(frame, (300, 250),  63, (0,0,255), -1)
#     cv.rectangle(frame, (100,100),(400,400),(0,255,0),-1, cv.LINE_AA)
#
#     # Display the resulting frame
#     cv.imshow('frame', frame )
#
#     if cv.waitKey(1) == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()
#-----------------------------------------------------



# Learn to handle mouse events in OpenCV
# You will learn these functions : cv.setMouseCallback()

# import cv2 as cv
# events = [i for i in dir(cv) if 'EVENT' in i]
# print( events )
#
# import numpy as np
# import cv2 as cv
# # mouse callback function
# def draw_circle(event,x,y,flags,param):
#     if event == cv.EVENT_LBUTTONDBLCLK:
#         cv.circle(img,(x,y),100,(255,0,0),-1)
# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv.namedWindow('image')
# cv.setMouseCallback('image',draw_circle)
# while(1):
#     cv.imshow('image',img)
#     if cv.waitKey(20) & 0xFF == 27:
#         break


# import numpy as np
# import cv2 as cv
# drawing = False # true if mouse is pressed
# mode = True # if True, draw rectangle. Press 'm' to toggle to curve
# ix,iy = -1,-1
# # mouse callback function
# def draw_circle(event,x,y,flags,param):
#     global ix,iy,drawing,mode
#     if event == cv.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix,iy = x,y
#     elif event == cv.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#             else:
#                 cv.circle(img,(x,y),5,(0,0,255),-1)
#     elif event == cv.EVENT_LBUTTONUP:
#         drawing = False
#         if mode == True:
#             cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#         else:
#             cv.circle(img,(x,y),5,(0,0,255),-1)
#
# img = np.zeros((512,512,3), np.uint8)
# cv.namedWindow('image')
# cv.setMouseCallback('image',draw_circle)
# while(1):
#     cv.imshow('image',img)
#     k = cv.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27:
#         break
# cv.destroyAllWindows()




