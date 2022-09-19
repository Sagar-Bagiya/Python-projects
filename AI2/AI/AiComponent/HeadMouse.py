import cv2
import mediapipe as mp
import pyautogui 
import numpy as np
import time

# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# For webcam input:
# drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
P_x, P_y = 0, 0
wscr, hscr = pyautogui.size()
wcam, hcam = 640, 480
cx, cy = wcam//2, hcam//2-80
w, h = 50, 50
Roi = {'start':(cx-w, cy-h),'end':(cx+w, cy+h)}
cap.set(3, wcam)
cap.set(4, hcam)
p_d_x, p_d_y = 0, 0

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()
    Y,X,shape = image.shape

    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image)

    # Draw the face mesh annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
      for face_landmarks in results.multi_face_landmarks:
        Hlandmark = face_landmarks.landmark[9]
        x,y =  Hlandmark.x, Hlandmark.y
        
        x,y = int(X*x), int(Y*y)
        cv2.rectangle(image, Roi['start'], Roi['end'], (0,0,255), 2)
        cv2.circle(image, (x,y), 3, (20,255,100), -1)

        m_x = np.interp(x, (Roi['start'][0], Roi['end'][0]), (1, wscr-1))
        m_y = np.interp(y, (Roi['start'][1], Roi['end'][1]), (1, hscr-1))
        d_x = m_x - P_x
        d_y = m_y - P_y
        # d_t = c_t - p_t
        print(d_x, d_y)

        if not(abs(d_x) == abs(p_d_x) and abs(d_y) == abs(p_d_y)) :
          m_x = P_x + d_x
          m_y = P_y + d_y
          pyautogui.moveTo(int(wscr-m_x), int(m_y))
          P_x,P_y = m_x,m_y

        p_d_x = d_x
        p_d_y = d_y
        
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
