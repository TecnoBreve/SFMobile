from socket import *

class Client:
    def connect_server(self, server, user):
        port = 80
        if server and user:
            try:
                self.cli = socket(AF_INET, SOCK_STREAM)
                self.cli.connect((server,port))
                return 'Conectado'
            except: return 'Conexão Invalida' 
        else: return 'Dados Invalidos'

    def enviarPedido(self, user, mesa, cmd, pedido):
        if pedido:
            try:
                msgPost = {'user': user,'cmd': cmd,'mesa': mesa,'pedido': pedido}
                self.cli.send(str(msgPost).encode())
            except Exception as e: print(e)