from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from login import Login
from mydatabase import Database
from styles import Styles

Builder.load_string("""
<History>:
    name: "History"
    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            canvas.before:
                Color:
                    rgba: root.bg_color
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint_y:None
            height: dp(60)
            Label:
                text: "History"
                font_name: "robotoblack.ttf"
                font_size: '20sp'
            AnchorLayout:
                anchor_x: "right"
                padding: [0,0,dp(30),0]
                Button:
                    canvas.before:
                        Rectangle:
                            pos: self.pos
                            size: self.size
                            source: "back.png"
                    size_hint:None,None
                    size: dp(35),dp(35)
                    background_normal: ""
                    background_color:0,0,0,0
                    on_press: root.goToHome()
        BoxLayout:
            ScrollView:
                do_scroll_y: True
                Label:
                    id: placeholder
                    color: root.secondary_color
                    text: "Hello World"
                    size_hint_y:None
                    height: self.texture_size[1]
                    text_size: self.width, None
                    padding: [dp(20),dp(20)]
                    
""")
class History(Screen):
    bg_color=Styles.primary_color
    secondary_color=Styles.secondary_color
    def on_pre_enter(self, *args):
        result=Database.getFacts(Login.getEmail())
        self.ids.placeholder.text=""
        for i in result:
            self.ids.placeholder.text+=i[2]
            self.ids.placeholder.text+="\n\n"
    def goToHome(self):
        self.manager.current="Home"