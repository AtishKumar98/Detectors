import cv2
from random import randrange

img_file = 'car.jpg'
video = cv2.VideoCapture('video1.mp4')
classfier_file = 'cars.xml'
ped_tracker_file = 'ped.xml'

while True:
    successfull_frame_read, frame = video.read()
    
    if successfull_frame_read:
        Black_white = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break


    # img1 = cv2.imread(img_file)
    # Black_white = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    car_tracer = cv2.CascadeClassifier(classfier_file)
    ped_tracker = cv2.CascadeClassifier(ped_tracker_file)


    # cars and peds 
    cars1 = car_tracer.detectMultiScale(frame)
    peds = ped_tracker.detectMultiScale(frame)

    print(cars1)

# Cars with particular Detect
# carsd = cars1[7]
# (x,y,w,h) = carsd 
# cv2.rectangle(img1, (x,y) , (x+w,y+h), (0,225,0),5)


    for (x,y,w,h) in cars1:

     cv2.rectangle(frame, (x,y) , (x+w,y+h), (0, 225, 225),1)

    for (x,y,w,h) in peds:

     cv2.rectangle(frame, (x,y) , (x+w,y+h), (0, 225, 0),3)

    cv2.imshow('Better picture', frame) 
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break
video.release()