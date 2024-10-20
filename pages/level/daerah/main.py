from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

from components.button import CustomButton

class LevelDaerah(Screen):
    def __init__(self, app, **kwargs):
        super(LevelDaerah, self).__init__(**kwargs)
        self.app = app
        
        layout = FloatLayout()
        
        background = Image(source="public/img/v2/home_screen/bg.png", 
                   size_hint=(1, 1), 
                   pos_hint={'center_x': 0.5, 
                             'center_y': 0.5})
        layout.add_widget(background)
        
        back_button = CustomButton(
            app=app,
            size_original=280,
            destination="choice_menu",
            source="public/img/v2/button/back.png",
            pos_hint={'center_x': 0.5, 'center_y': 0.11},
            allow_stretch=True,
            keep_ratio=True
        )
        layout.add_widget(back_button)
        
        self.add_widget(layout)
        