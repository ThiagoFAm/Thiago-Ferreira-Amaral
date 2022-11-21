#from itertools import count
import cv2
import os
import imutils
import time

nome = input(str('Nome:'))
dirPasta = '/home/ia/Desktop/P6_1/Raspberry_webcam/Fotos'
dirPasta_nome = dirPasta + '/' + nome

if not os.path.exists(dirPasta_nome):
    print('Pasta Gerada: ' + dirPasta_nome)
    os.makedirs(dirPasta_nome)
    
detectorRosto = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

contadorFotos = 0

while True:
    ret, frame = cam.read()
    frame = imutils.resize(frame, width=640)
    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    RecoFacial = detectorRosto.detectMultiScale(frameCinza, scaleFactor=1.2, minNeighbors = 5)

    for (x,y,w,h) in RecoFacial:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)
        rosto = auxFrame[y:y+h, x:x+w]
        rosto = cv2.resize(rosto, (150,150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(dirPasta_nome + f'/rosto_{contadorFotos}.jpg',rosto)
        contadorFotos = contadorFotos + 1
    cv2.imshow('frame',frame)

    k = cv2.waitKey(1)

    if k == 27 or contadorFotos >= 150:
        break
cam.release()
cv2.destroyAllWindows