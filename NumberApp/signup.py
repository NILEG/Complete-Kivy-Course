from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from styles import Styles
from mydatabase import Database
Builder.load_string("""
#: import CTextInput custom_widgets
#: import CButton custom_widgets
<Signup>:
    name: "signup"
    BoxLayout:
        orientation: "vertical"
        padding: dp(40)
        BoxLayout:
            size_hint:1,0.4
            Image:
                source: "background.png"
        AnchorLayout:
            size_hint: 1,0.6
            anchor_y: "top"
            BoxLayout:
                orientation: "vertical"
                size_hint_y:None
                spacing: dp(10)
                height: self.minimum_height
                Label:
                    text: "Create your Account"
                    color: root.seconday_color
                    halign: "left"
                    text_size: self.size
                    font_name: "robotoblack.ttf"
                CTextInput:
                    id: email
                    hint_text: "Email"
                    size_hint_y:None
                    height: dp(50)
                CTextInput:
                    id: password
                    hint_text: "Password"
                    size_hint_y:None
                    height: dp(50)
                CTextInput:
                    id: cpassword
                    hint_text: "Confirm Password"
                    size_hint_y:None
                    height: dp(50)
                CButton:
                    text: "Signup"
                    on_press: root.createEntry()
                    size_hint_y:None
                    height: dp(50)
""")
class Signup(Screen):
    seconday_color=Styles.secondary_color
    def createEntry(self):
        email=self.ids.email.text
        password=self.ids.password.text
        cpassword=self.ids.cpassword.text
        if(password==cpassword):
            if(Database.isValid(email)):
                Database.insertdata(email,password)
                self.manager.current="login"
            else:
                print("Email already exists")