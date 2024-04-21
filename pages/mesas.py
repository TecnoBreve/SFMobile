import streamlit as st
from sqlite3 import connect

conn = connect('src/dados.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS TEMP (ID INTEGER PRIMARY KEY AUTOINCREMENT, MESA TEXT, COMANDA TEXT)')

st.title('SalesForce Mobile')
cmd = st.text_input('Comanda')
mesa = st.text_input('Mesa')

if st.button('Pedido'):
    c.execute(f'INSERT INTO TEMP(MESA, COMANDA) VALUES("{mesa}","{cmd}")')
    conn.commit()
    st.switch_page('pages/pedido.py')