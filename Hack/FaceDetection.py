import numpy as np
import cv2

path = '/Users/Legend/anaconda2/lib/python2.7/site-packages/cv2/data/'
face_cascade = cv2.CascadeClassifier(path + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(path + 'haarcascade_eye.xml')
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()