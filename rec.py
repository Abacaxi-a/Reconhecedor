import cv2
from deepface import DeepFace
import os
from tkinter import *
from modulos.local import localizar
import time

ft = 'img.jpg'

class proc(localizar):
    def __init__(self,master=None):
        self.procurar = 'procurar'
        self.arquivo = ft
        self.master = Frame(master)
        self.find()
        self.comparar()
        self.info()
        self.tela = Frame(self.master).pack()
        self.texto = Label(self.tela, text=f'{self.a}\n').pack()
        self.texto2 = Label(self.tela, text=f'{self.i} {self.r2}\n').pack()
        self.texto3 = Label(self.tela, text=f'age: {self.b}\n').pack()

root = Tk()
proc(root)
root.mainloop()
