from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Interface_2(BoxLayout):
    def sliding(self, obj):
        print(obj.value)
class Interface(BoxLayout):
    def checking(self, checkbox, labelID):
        if(checkbox.active):
            print(labelID.text)

class WidgetsApp(App):
    pass

WidgetsApp().run()