from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ListProperty
from kivy.uix.progressbar import ProgressBar

Builder.load_string("""

<CustomProgressBar>:
    id: pb
    canvas:
        BorderImage:
            border:0,0,0,0
            pos: pb.x, pb.center_y-root.bgBarHeight/2
            size: self.width, root.bgBarHeight
            source: root.background_image
        BorderImage:
            pos: pb.x, pb.center_y - root.fgBarHeight/2
            border:0,0,0,0
            size: pb.width * (pb.value / float(pb.max)), root.fgBarHeight
            source: root.foreground_image
    Label:
        text: str(int(pb.value))+"%" if root.showProgress else ""
        pos: pb.center_x-self.texture_size[0]/2,pb.center_y-self.texture_size[1]/2
        size: self.texture_size
        color:root.textColor
        font_size: root.fontSize
""")

class CustomProgressBar(ProgressBar):
    background_image = StringProperty("") #Background Image used as Color
    foreground_image = StringProperty("")#Foreground Image used as Color
    bgBarHeight = NumericProperty(dp(10))#Height of background Image
    fgBarHeight = NumericProperty(dp(10))#Height of foreground Image
    fontSize=NumericProperty(dp(10))#Font Size of Progress Text
    showProgress=BooleanProperty(False)#Progress Text will be visible only if showProgress Property is true
    textColor=ListProperty([0,0,0,1])#Color of the Progress Text

