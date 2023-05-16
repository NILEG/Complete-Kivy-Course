from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
from kivy.lang import Builder
from kivy.properties import StringProperty, BoundedNumericProperty, NumericProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
Builder.load_string("""
<Infographic>:
    size_hint:None,None
    size: self.radius+(self.bg_thickness*2), self.radius+(self.bg_thickness*2)
    canvas:
        Color:
            rgba:self.bg_color
        Line:
            width: self.bg_thickness
            ellipse:(self.pos[0]+self.bg_thickness, self.pos[1]+self.bg_thickness, self.radius, self.radius)
        Color:
            rgba:self.fg_color
        Line:
            width: self.fg_thickness
            ellipse:(self.pos[0]+self.bg_thickness, self.pos[1]+self.bg_thickness, self.radius, self.radius, 0, (self.percentage*360)/100)
<Custombtn>:
    bgColor:(1,1,1,1)
    canvas.before:
        Color:
            rgba: self.bgColor
        Ellipse:
            size:self.size
            pos:self.pos

""")
class Infographic(Widget):
    bg_thickness=NumericProperty(10)
    fg_thickness=NumericProperty(8)
    bg_color=ListProperty([1,1,1,1])
    fg_color=ListProperty([0,0,0,1])
    radius=NumericProperty(50)
    percentage=BoundedNumericProperty(0, min=0, max=100)
class Custombtn(ButtonBehavior, Label):
    pass

class MainInterface(FloatLayout):
    def clicking(self):
        print("Working...")
class CustomBoxLayout(BoxLayout):
    hex_code=StringProperty("#FFFFFF")
    alpha=BoundedNumericProperty(1)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.creating_rect)
        Clock.schedule_interval(self.updating, 1/30)
    def updating(self, dt):
        self.rect.pos=self.pos
        self.rect.size=self.size
    def creating_rect(self, dt):
        with self.canvas.before:
            r,g,b,a=get_color_from_hex(self.hex_code)
            Color(rgba=(r,g,b, self.alpha))
            self.rect=Rectangle(pos=self.pos, size=self.size)
class Interface_2(FloatLayout):
    pass
class Interface(FloatLayout):
    pass
class DrawingApp(App):
    pass

DrawingApp().run()