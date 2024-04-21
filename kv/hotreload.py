from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.list import OneLineListItem

class LoginWin(MDScreen): ...
class MainWin(MDScreen): ...
class Produtos(MDScreen): ...

class SalesForce(MDApp):
    KV_FILES = ['src/style.kv']
    DEBUG = True
    def build_app(self):
        Builder.load_file('src/style.kv')
        th = self.theme_cls
        th.theme_style = 'Dark'
        th.primary_palette = 'Red'
        sm = MDScreenManager()
        sm.add_widget(Produtos())
        sm.add_widget(MainWin())
        sm.add_widget(LoginWin())
        return sm
        
    def on_start(self):
        self.root.current = 'prodwin'
        self.idsMain = self.root.get_screen('mainwin').ids
        self.idsProd = self.root.get_screen('prodwin').ids
        print(self.idsProd)
        for i in range(21):
            self.idsProd.container.add_widget(OneLineListItem(text=f"Single-line item {i}"))


SalesForce().run()