from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line

from components.button import ButtonPlaying

class ImageWithBorder(Image):
    def __init__(self, **kwargs):
        super(ImageWithBorder, self).__init__(**kwargs)

        with self.canvas.before:
            Color(1, 0, 0, 1) 
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=2)

        self.bind(pos=self.update_border, size=self.update_border)

    def update_border(self, *args):
        self.border.rectangle = (self.x, self.y, self.width, self.height)


class MainMenuScreen(Screen):
    def __init__(self, app, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)
        
        layout = FloatLayout()

        background = Image(source="public/img/v2/home_screen/bg.png", 
                   size_hint=(1, 1), 
                   pos_hint={'center_x': 0.5, 
                             'center_y': 0.5})
        layout.add_widget(background)
        
        info = Image(source="public/img/v2/home_screen/info.png", 
                     pos_hint={'center_x': 0.5, 
                               'center_y': 0.5})
        layout.add_widget(info)

        button_play = ButtonPlaying(
            app=app,
            size_original=250,
            source="public/img/v2/button/play.png",
            pos_hint={'center_x': 0.5, 
                      'center_y': 0.11},
        )
        layout.add_widget(button_play)
    
        self.add_widget(layout)
        
        self.app = app