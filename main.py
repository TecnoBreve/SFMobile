from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.toast import toast
from kivymd.uix.list import OneLineListItem, CheckboxLeftWidget
from kivymd.uix.label import MDLabel
from socket import *

class LoginWin(MDScreen): ...
class MainWin(MDScreen): ...
class Produtos(MDScreen): ...

class SalesForce(MDApp):
    def build(self):
        Builder.load_file('src/style.kv')
        tm = self.theme_cls
        tm.theme_style = 'Dark'
        tm.primary_palette = 'Red'
        sm = MDScreenManager()
        sm.add_widget(LoginWin())
        sm.add_widget(MainWin())
        sm.add_widget(Produtos())
        return sm

    def on_start(self):
        self.root.current = 'loginwin'
        self.idsMain = self.root.get_screen('mainwin').ids
        self.idsProd = self.root.get_screen('prodwin').ids
        produtos = [
            'Chopp Trad. 550ml',
            'Chopp Trad. 330ml',
            'Chopp Vinho 550ml',
            'Chopp Vinho 330ml',
            'Com borda',
        ]
        for item in produtos:
            self.idsProd.cont.add_widget(
                OneLineListItem(
                    text=item, on_release=lambda x: self.addProd(x)
                )
            )
        self.pedido = []

    def addProd(self, x):
        item = x.text
        if item:
            self.idsProd.contBefore.add_widget(
                OneLineListItem(
                    text=item, 
                    )
            )
            self.pedido.append(item)

    def connServer(self, server, uid):
        self.user = uid
        try:
            self.cli = socket(AF_INET, SOCK_STREAM)
            self.cli.connect((server,44421))
            self.root.current = 'mainwin'
        except Exception as e: 
            toast(f'Conexão Invalida - {e}')

    def enviarPedido(self):
        if self.pedido:
            try:
                msgPost = {
                    'user': self.user,
                    'cmd': self.cmd,
                    'mesa': self.mesa,
                    'pedido': self.pedido
                }
                self.cli.send(str(msgPost).encode())
                toast('Pedido enviado com Sucesso')
                self.root.current = 'mainwin'
            except: 
                self.root.current = 'loginwin'
                toast('Reconecte-se')

    def changeProd(self, mesa, cmd):
        if mesa and cmd:
            self.mesa = mesa
            self.cmd = cmd
            self.idsProd.lblDados.text = f'Mesa: {mesa} | Comanda {cmd}'
            self.root.current = 'prodwin'
        else: toast('Valores Icorretos!')

    def clearList(self):
        self.idsProd.contBefore.clear_widgets()
        self.idsProd.contBefore.add_widget(MDLabel(text='Pedido Atual:',halign = 'center'))
        self.pedido = []

if __name__ == '__main__':    
    SalesForce().run()