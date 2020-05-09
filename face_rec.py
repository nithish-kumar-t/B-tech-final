import face_recognition
import cv2
import numpy as np
import os
video_capture = cv2.VideoCapture(0)
#obama_image = face_recognition.load_image_file("obama.jpg")
#obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
#biden_image = face_recognition.load_image_file("biden.jpg")
#biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
#known_face_encodings = [
#    obama_face_encoding,
#    biden_face_encoding
#]
#known_face_names = [
#    "Barack Obama",
#    "Joe Biden"
#]
##getting the saved pictures and encoding it 
known_face_encodings=[]
known_face_names=[]
dictory=os.getcwd()
pictures=os.path.join(dictory,'pictures')
for i in os.listdir(pictures):
    print(i)
    image=face_recognition.load_image_file(i)
    encoding =face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(i.split('.')[0])
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()
    #making the frame small for better speed and stuff
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    #delaying and taking a input to either quit or save the frame
    key=cv2.waitKey(1)
    if (key==ord('q')):
        break
    elif(key==ord('s')):
        cv2.imwrite(os.path.join(pictures,'something.png'),frame)
    #processing the frame
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        #doing the fancy matching thingy
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
    process_this_frame = not process_this_frame

    #viewing the finished output
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    cv2.imshow('Video', frame)



# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
