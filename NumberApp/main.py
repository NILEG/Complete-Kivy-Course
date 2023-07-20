from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from history import History
from signup import Signup
from login import Login
from mydatabase import Database
from home import Home
Window.softinput_mode = "below_target"
class Interface(ScreenManager):
    def __init__(self, **kwargs):
        Window.bind(on_keyboard=self.quit)
        super().__init__(**kwargs)
        try:
            Database.connectDatabase()
        except Exception as e:
            print(e)
        login=Login()
        signup=Signup()
        home=Home()
        history=History()
        self.add_widget(login)
        self.add_widget(signup)
        self.add_widget(home)
        self.add_widget(history)
    def quit(self, window, key,  *args):
        if(key==27):
            App.get_running_app().stop()
class NumberApp(App):
    pass

NumberApp().run()