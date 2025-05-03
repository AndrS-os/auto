from os import write
from numpy.core.fromnumeric import size
import streamlit as st; 
import Controller.clientesController as clientesController
import models.clientes as clientes

st.title("incluir cliente")



with st.form(key="include_cliente"):
    input_name = st.text_input(label="insira o seu nome")
    input_age = st.number_input(label="insira su idade",format="%d",step=1)
    input_occupation = st.selectbox(label="selecione sua profissão", options=["musico","cantor","designer","promotor"])
    input_button_submit =st.form_submit_button("eviar")
    
if input_button_submit:
        st.write(f'nome: {input_name}')    
        st.write(f'idade: {input_age}')    
        st.write(f'nome: {input_occupation}')    
