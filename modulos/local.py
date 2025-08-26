import os
import cv2
from deepface import DeepFace
from tkinter import *
import pandas as pd
import time

class localizar:
    def __init__(self, image_path):
        self.arquivo = image_path

    def find(self):
        self.img = cv2.imread(self.arquivo)
        self.r = DeepFace.find(img_path=self.img,db_path=self.procurar,enforce_detection=False)
        self.a = pd.DataFrame(self.r[0])
        self.a = self.a['identity']
        return self.a
    
    def comparar(self):
        for self.i in self.a:
            if 'jpg' in self.i:
                self.r2 = DeepFace.verify(self.img, self.i,enforce_detection=False)
                self.r2 = self.r2['verified']
                return self.r2
            else:
                self.r2 = 'imagem exata ou semelhante não encontrada'
                return ''
    
    def info(self):
        self.r3 = DeepFace.analyze(img_path=self.i,actions=('age'),enforce_detection=False,)
        self.b = pd.DataFrame(self.r3)
        self.b = self.b['age'][0]
        return self.b
        