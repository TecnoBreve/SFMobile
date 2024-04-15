from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from socket import *

class LoginWin(MDScreen): ...
class MainWin(MDScreen): ...

class SalesForce(MDApp):
    def build(self):
        Builder.load_file('src/style.kv')
        tm = self.theme_cls
        tm.theme_style = 'Dark'
        tm.primary_palette = 'Red'
        sm = MDScreenManager()
        sm.add_widget(LoginWin())
        sm.add_widget(MainWin())
        return sm

    def connServer(self, server, uid):
        self.user = uid
        try:
            self.cli = socket(AF_INET, SOCK_STREAM)
            self.cli.connect((server,44421))
            print('Concetado com Sucesso')
            self.root.current = 'mainwin'
        except Exception as e: 
            print(e)


    def enviarMsg(self, msg):
        try:
            msgPost = str({'user':self.user, 'text':msg})
            self.cli.send(msgPost.encode())
        except: 
            self.root.current = 'loginwin'
            print('Reconecte')
SalesForce().run()