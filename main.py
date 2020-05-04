"""import cv2
import face_recognition
cap=cv2.VideoCapture(0)
while True:
    ret,frame =cap.read()
    cv2.imshow('frame',frame)
    key=cv2.waitKey(1)
    if(key== ord('q')):
        break
    elif(key== ord('s')):
        cv2.imwrite('something.jpg',frame)
cap.release()
cv2.destroyAllWindows()"""
