from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.tools.hotreload.app import MDApp

class LoginWin(MDScreen): ...
class MainWin(MDScreen): ...

class SalesForce(MDApp):
    KV_FILES = ['src/style.kv']
    DEBUG = True
    def build_app(self):
        Builder.load_file('src/style.kv')
        th = self.theme_cls
        th.theme_style = 'Dark'
        th.primary_palette = 'Red'
        sm = MDScreenManager()
        sm.add_widget(MainWin())
        sm.add_widget(LoginWin())
        return sm

SalesForce().run()