import cv2
from urllib.request import urlopen
import numpy as np
from PIL import Image
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

detector_facial = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("/home/ia/Desktop/P6_1/Esp32cam_Raspberry/ClassRASP_LBPH.yml")

url = r'http://192.168.4.3/capture'

while True:
    img_resp = urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype="uint8")
    img = cv2.imdecode(imgnp, -1)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rostos_encontrados = detector_facial.detectMultiScale(img_gray, scaleFactor = 1.4, minSize=[90,90], maxSize=[100,100], minNeighbors = 3)

    for x,y,w,h in rostos_encontrados:
        print('Rosto: {},{}'.format(w,h))
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        image_face = cv2.resize(img_gray[y:y + w, x:x + h], (220, 220))

        
        id, face = face_recognizer.predict(image_face)
        
        print(id)

        if id == 0:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            name = 'Thiago'
            cv2.putText(img, name,(x,y + (w + 30)), cv2.FONT_HERSHEY_COMPLEX_SMALL,  2, (0,255,0))
            
            GPIO.setmode(GPIO.BCM)    
            GPIO.setup(2, GPIO.OUT)                                     
            GPIO.output(2, False)
            time.sleep(1)
            GPIO.output(2, True)
            
        
        elif id == 1:
            cv2.rectangle(img, (x, y), (x + w,  y + h), (0, 0, 255), 2)
            name = 'intruso'
            cv2.putText(img, name,(x,y + (w + 30)), cv2.FONT_HERSHEY_COMPLEX_SMALL,  2, (0,0,255))
        
    cv2.imshow("ESP32_CAM", img)
    
    if cv2.waitKey(1) == ord('q'):
        break

