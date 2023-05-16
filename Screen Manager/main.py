from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition, WipeTransition, SwapTransition, RiseInTransition, \
    FallOutTransition


class Interface(ScreenManager):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.transition=FallOutTransition()
    def switching_back(self):
        self.transition.duration=0.5
        self.current="Main Screen"
    def switching(self):
        print(self.current_screen)
        self.transition.duration = 0.5
        #self.transition.direction = "left"
        self.current="Profile"
        print(self.current_screen)
class ScrmanagerApp(App):
    pass
ScrmanagerApp().run()
