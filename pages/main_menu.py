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
        self.app = app
        
        layout = FloatLayout()
        
        self.background = Image(source="public/img/v2/home_screen/bg.png", 
                    pos_hint={'center_x': 0.5, 
                             'center_y': 0.5},
                    allow_stretch=True,
                    keep_ratio=True)
        layout.add_widget(self.background)
        
        self.info = Image(source="public/img/v2/home_screen/info.png", 
                    pos_hint={'center_x': 0.5, 
                            'center_y': 0.5},
                    allow_stretch=True,
                    keep_ratio=True)
        layout.add_widget(self.info)

        self.button_play = ButtonPlaying(
            app=app,
            size_original=280,
            source="public/img/v2/button/play.png",
            pos_hint={'center_x': 0.5, 
                      'center_y': 0.11},
        )
        layout.add_widget(self.button_play)
        
        self.add_widget(layout)