import cv2 
from random import randrange

trained_face_data = cv2.CascadeClassifier('face.xml')

# Image for read
# img = cv2.imread('img.jpg')
webcam = cv2.VideoCapture(0)
while True:
    successfull_frame_read, frame = webcam.read()


#for grayscale image 
    # grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    # cv2.imshow("FaceD", grayscaled_frame)
    # cv2.waitKey(1)




# detect faces 

    face_coordinates = trained_face_data.detectMultiScale(frame)


    for (x,y,w,h) in face_coordinates:

     cv2.rectangle(frame, (x,y) , (x+w,y+h), (randrange(120, 225),randrange(120, 225),randrange(120,225)),5)

    # (x,y,w,h) = face_coordinates[1]

    # cv2.rectangle(frame, (x,y) , (x+w,y+h), (0,0,225),5)

    # print (face_coordinates)



    cv2.imshow("FaceD", frame)
    key = cv2.waitKey(1)

    if key==81 or key==113:
            break
webcam.release()

