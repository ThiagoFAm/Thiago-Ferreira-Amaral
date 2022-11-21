import cv2
import os
import RPi.GPIO as GPIO
import time
                                       
                                                          
GPIO.setwarnings(False)                                 
                       

dataPath = '/home/ia/Desktop/P6_1/Raspberry_webcam/Fotos' 
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)


faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.read('/home/ia/Desktop/P6_1/Esp32cam_Raspberry/ClassRASP_LBPH.yml')

cap = cv2.VideoCapture(0)


while True:
    ret,frame = cap.read()

    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        face = auxFrame[y:y+h,x:x+w]
        face = cv2.resize(face,(150,150),interpolation= cv2.INTER_CUBIC)
        result = face_recognizer.predict(face)
        
        print(result)
        
        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            
        if result[0] == 0:
            cv2.putText(frame,'Thiago',(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            GPIO.setmode(GPIO.BCM)    
            GPIO.setup(2, GPIO.OUT)                                     
            GPIO.output(2, False)
            time.sleep(1)                                      
            GPIO.output(2, True)
        
            
        elif result[0] == 1:
            cv2.putText(frame,'Intruso',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        
        
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == 113: break
cap.release()
cv2.destroyAllWindows()