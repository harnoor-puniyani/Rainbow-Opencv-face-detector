import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#giving the image to the algorithm
img = cv2.imread('katrina_face.jpg')


#converting image to gfrayscale
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detect-faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled)

#drawing rectangle around the face => face_coordiantes returns x,y,w,h
#to detect multiple faces we will user loop
#(x,y,w,h)=face_coordinates[0]
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img , (x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),3)

#showing the image
cv2.imshow("Harnoor's AI Detection",img)
#waits until a key is pressed
cv2.waitKey()

print('code completed')