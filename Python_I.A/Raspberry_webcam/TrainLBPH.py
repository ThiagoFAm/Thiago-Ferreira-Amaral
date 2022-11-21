
import cv2 
import os
import numpy as np

dirPasta = '/home/ia/Desktop/P6_1/Raspberry_webcam/Fotos'
lista = os.listdir(dirPasta)
print('Pessoas Cadastradas: ', lista)

ids = []
faces = []
id = 0

for nomeDir in lista:
    pessoaDir = dirPasta + '/' + nomeDir    


    for file in os.listdir(pessoaDir):
        print(f'Rosto: ', nomeDir + '/' + file)
        ids.append(id)
        faces.append(cv2.imread(pessoaDir + '/' + file, 0))
        
    id = id + 1

LBPH = cv2.face.LBPHFaceRecognizer_create(radius = 5,grid_x = 10,grid_y = 10)

LBPH.train(faces, np.array(ids))
LBPH.write('/home/ia/Desktop/P6_1/Raspberry_webcam/ClassRASP_LBPH.yml')
