import cv2
from deepface import DeepFace
from tkinter import *
import pandas as pd
import numpy as np
from PIL import Image
from io import BytesIO

class localizar:
    def byting(self,arquivo):
        imagem = Image.open(arquivo)
        buf = BytesIO()
        imagem.save(buf, format="PNG")
        byte_im = buf.getvalue()
        self.img = cv2.imdecode(np.frombuffer(byte_im, np.uint8), cv2.IMREAD_UNCHANGED)

    def find(self):
        self.r = DeepFace.find(self.img,db_path=self.procurar,enforce_detection=False)
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
        