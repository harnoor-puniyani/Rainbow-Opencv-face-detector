import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#videoCapture(0) opens webcam
webcam = cv2.VideoCapture(0)

#video read frames , hence the loop
while True:
    # reading frame
    successful_frame_read , frame=webcam.read()

    # must convert to grayscale
    grayscale_img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    #detect faces
    face_coordinates= trained_face_data.detectMultiScale(grayscale_img)

    #drawing rectangle
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),3)
    

    
    cv2.imshow("Harnoor's webcam",frame)
    #waitkey will wait for 1ms
    key=cv2.waitKey(1)

    #stopping | press q to quit
    if key==133 or key==81:
        webcam.release()
        break
#releasing webcam
webcam.release()

# key = cv2.waitkey()

print('code Completed!')