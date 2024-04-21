import streamlit as st
from sqlite3 import connect
from cliente import Client

conn = connect('src/dados.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS LOGINS(ID INTEGER PRIMARY KEY AUTOINCREMENT, SERVIDOR TEXT, USUARIO TEXT)')
cl = Client()

st.title('Login Servidor')

server = st.text_input('Servidor', value='localhost')
user = st.text_input('Usuário')

if st.button('Logar'): 
    connS = cl.connect_server(server, user)
    if connS != 'Conexão Invalida' and connS != 'Dados Invalidos': 
        st.toast(conn)
        c.execute(f'INSERT INTO LOGINS(SERVIDOR, USUARIO) VALUES("{server}","{user}")')
        conn.commit()
        c.close()
        cl.cli.close()
        st.switch_page("pages/mesas.py")
    else: st.error(conn)