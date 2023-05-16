from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

from Custom_Layouts import BgBoxLayout, BgAnchorLayout, BgGridLayout, BgStackLayout

class Intefcae_6(PageLayout):
    pass
class Intercae_5(BgBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.create)
    def create(self, dt):
        for i in range(10):
            btn=Button(text=str(i), size_hint=(None,None), size=(dp(100),dp(50)))
            self.ids.stackLayout.add_widget(btn)

    def clear(self):
        self.ids.stackLayout.clear_widgets()

    def generate(self):
        for i in range(10):
            btn=Button(text=str(i), size_hint=(None,None), size=(dp(100),dp(50)))
            self.ids.stackLayout.add_widget(btn)
class Interface_4(BgAnchorLayout):
    pass
class Interface_3(BgBoxLayout):
    def shuffle(self):
        textList=list()
        count=8
        children=self.ids.gridLayout.children
        for child in reversed(children):
            textList.append(child.text)

        print(textList)
        for r in range(3, 0, -1):
            for j in range(r-1, r+2*3, 3):
                children[count].text= textList[j]
                count-=1
class Interface_2(BgBoxLayout):
    pass
class Interface(BgAnchorLayout):
    pass
class LayoutsApp(App):
    pass

LayoutsApp().run()