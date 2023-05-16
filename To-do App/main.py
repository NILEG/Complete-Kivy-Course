from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.textinput import TextInput

store = JsonStore('data.json')
class Custombtn(Button):
    key_name=StringProperty()
class Interface(ScreenManager):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.fetching_data)
    def truncate_string(self, str_input, max_length):
        str_end = '...'
        length = len(str_input)
        if length > max_length:
            return str_input[:max_length - len(str_end)] + str_end
        else:
            return str_input
    def deleting(self, obj_btn):
        id=obj_btn.key_name
        self.ids.gridLayout.remove_widget(self.ids[id])
        store.delete(id)
    def fetching_data(self, dt):
        try:
            keys=store.keys()
            for key in keys:
                layout = BoxLayout(spacing=dp(10), size_hint_y=None, height=dp(80))
                self.ids[key]=layout
                title = Custombtn(background_normal="orange.png", key_name=key, font_name= "robotolight.ttf", text=self.truncate_string(key, 10))
                delete = Custombtn(key_name=key,on_press=self.deleting, background_normal="delete_icon.png", size_hint=(None, None), size=(dp(80), dp(80)))
                title.bind(on_press=self.detail_screen)
                layout.add_widget(title)
                layout.add_widget(delete)
                self.ids.gridLayout.add_widget(layout)
        except Exception as e:
            print(e)
    def back_btn(self):
        self.current = "Main Screen"
        store.put(self.ids.noticeTitle.text, data=self.ids.inputData.text)
    def detail_screen(self, btn_obj):
        self.ids.noticeTitle.text=btn_obj.key_name
        self.ids.inputData.text=store.get(btn_obj.key_name)["data"]
        self.current="Details Screen"
    def addItem(self, obj):
        self.popup.dismiss()
        layout=BoxLayout(spacing=dp(10), size_hint_y=None, height=dp(80))
        title=Custombtn(background_normal="orange.png", font_name= "robotolight.ttf", key_name=self.textInput.text, text=self.truncate_string(self.textInput.text, 10))
        delete=Custombtn(on_press=self.deleting, key_name=self.textInput.text, background_normal="delete_icon.png", size_hint=(None,None), size=(dp(80), dp(80)))
        self.ids[self.textInput.text]=layout
        title.bind(on_press=self.detail_screen)
        layout.add_widget(title)
        layout.add_widget(delete)
        store.put(self.textInput.text, data="")
        self.ids.gridLayout.add_widget(layout)
    def show_popup(self):
        layout=BoxLayout(orientation="vertical", padding=dp(16), spacing=dp(10))
        btn=Button(background_normal="red.png", text="Submit",font_name= "robotolight.ttf",)
        btn.bind(on_press=self.addItem)
        self.textInput=TextInput(multiline=False)
        layout.add_widget(self.textInput)
        layout.add_widget(btn)
        self.popup=Popup(title_font="robotoblack.ttf", title="Notice Title", size_hint=(0.8,None), height=dp(180), content=layout)
        self.popup.open()
class TodoApp(App):
    pass

TodoApp().run()