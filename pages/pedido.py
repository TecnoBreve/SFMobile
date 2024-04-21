from sqlite3 import connect
import streamlit as st
from login import enviarPedido
from cliente import Client

conn = connect('src/dados.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS PEDIDOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, MESA TEXT, COMANDA TEXT, PEDIDO TEXT)')
temp = c.execute('SELECT MESA, COMANDA FROM TEMP ORDER BY ID DESC').fetchone()
login = c.execute('SELECT USUARIO, SERVIDOR FROM LOGINS ORDER BY ID DESC').fetchone()
cl = Client()

mesa = temp[0]
cmd = temp[1]
user = login[0]
server = login[1]
cl.connect_server(server, user)

st.title('Pedidos')

produtos = ['Chopp 550ml','Chopp 550ml com borda',]

selecao = st.multiselect('Produtos *', produtos)
obs = st.text_input('Observação?')
st.divider()

if st.button('Enviar Pedido'):
    if selecao: print(selecao)
    cl.enviarPedido(user, mesa, cmd, selecao)
    cl.cli.close()
    st.switch_page('pages/mesas.py')

