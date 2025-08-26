# from modulos.local import localizar
# from deepface import DeepFace
# import cv2
# import os
import time
# import pandas as pd
import customtkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD

# df = pd.read_pickle(r'procurar\representations_vgg_face.pkl')
# print(df)

def callback(teste):
    print(teste)

def on_drop(event,label:tk.CTkFrame,frame:tk.CTkFrame):
    file_path_image = event.data.strip()
    label.configure(text=f"Arquivo recebido:\n{file_path_image}")
    label.after(2000, lambda: label.configure(text=f"Iniciando analize"))
    label.after(2000, lambda: frame.place_forget())

def tela_imagem():
    #-------------INSERIR IMAGEM-------------------- 
    frame2 = tk.CTkFrame(app)
    frame2.place(relx=0.5, rely=0.5, anchor="center")

    label = tk.CTkLabel(frame2, text='Arraste arquivo aqui', width=300, height=100)
    label.place(relx=0.5, rely=0.5, anchor="center")
    # Registrar o label como alvo de drop
    label.drop_target_register(DND_FILES)
    label.dnd_bind('<<Drop>>', lambda x: on_drop(x,label,frame2))


def Acesso(app,frame_inicial:tk.CTkFrame):
    app.geometry("1440x720")
    frame_inicial.place_forget()
    tela_imagem()
    

if __name__ == '__main__':
    # Use TkinterDnD.Tk() para habilitar drag and drop
    app = TkinterDnD.Tk()
    tk.set_appearance_mode("light")  # ou "dark"
    app.geometry("400x250")

    #---------------TELA INICIAL--------------------
    frame1 = tk.CTkFrame(app)
    frame1.place(relx=0.5, rely=0.5, anchor="center")
    button = tk.CTkButton(frame1, text='Analizar', command=lambda: Acesso(app,frame1))
    button.grid(row=0, column=2, padx=20, pady=20)
    app.mainloop()


# class proc(localizar):
#     def __init__(self,master=None):
#         self.procurar = 'procurar'
#         self.arquivo = ft
#         self.master = Frame(master)
#         self.find()
#         self.comparar()
#         self.info()
#         self.tela = Frame(self.master).pack()
#         self.texto = Label(self.tela, text=f'{self.a}\n').pack()
#         self.texto2 = Label(self.tela, text=f'{self.i} {self.r2}\n').pack()
#         self.texto3 = Label(self.tela, text=f'age: {self.b}\n').pack()

# root = Tk()
# proc(root)
# root.mainloop()
