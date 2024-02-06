from modulos.local import localizar
import streamlit as st
import numpy as np


class proc(localizar):
    def __init__(self):
        st.set_page_config(page_title='teste')

        with st.container():   
            self.procurar = 'procurar'
            self.arquivo = st.file_uploader('Insira a imagem:',['jpeg','jpg'])
            if not self.arquivo == None:
                st.image(self.arquivo,width=200)
                self.byting(self.arquivo)
            else:    
                pass

        with st.container():
            if not self.arquivo == None:
                st.image(self.find()[0], width=200)
                st.write(self.find(),self.comparar())
        #     self.info()

proc()
