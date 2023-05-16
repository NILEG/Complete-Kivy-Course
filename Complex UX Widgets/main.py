from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager

class Pup_up(Popup):
    pass
class DropdownMenu(DropDown):
    def btn1(self):
        Interface.dropdown.dismiss()
        App.get_running_app().root.current="Profile"

class Interface(ScreenManager):
    dropdown=None
    def show(self):
        Pup_up().open()
    def show_menu(self):
        Interface.dropdown=DropdownMenu()
        Interface.dropdown.open(self.ids.btn)
class ComplexwidgetsApp(App):
    pass

ComplexwidgetsApp().run()