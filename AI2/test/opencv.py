import cv2
import face_recognition

dhoni = cv2.imread(r'D:\python project\AI2\test\dhoni.jpg')
# mesi = cv2.imread(r'D:\python project\AI2\test\mesi3.jpg')

dhoniencode = face_recognition.face_encodings(dhoni)[0]
# mesiencode = face_recognition.face_encodings(mesi)[0]

result = face_recognition.face_locations(dhoni)
top, right, bottom, left = result[0]

top *= 1
right *= 1
bottom *= 1
left *= 1

cv2.rectangle(dhoni,(left, top),(right, bottom),(0,0,255),2)
# cv2.imshow("my dhoni",dhoni)
cv2.rectangle(dhoni, (left+20, bottom - 20), (right-20, bottom), (0, 0, 255), cv2.FILLED)

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(dhoni, "dhoni bhai", (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

cv2.imshow("my window",dhoni)
cv2.waitKey(0)