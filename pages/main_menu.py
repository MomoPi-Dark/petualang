from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout

from components.button import CustomButton, CustomImage

class MainMenuScreen(Screen):
    def __init__(self, app, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)
        self.app = app
        
        layout = FloatLayout()

        background = Image(source="assets/img/home_screen/bg.png", 
                    size_hint=(1, 1), 
                    allow_stretch=True,
                    keep_ratio=True,
                    pos_hint={'center_x': 0.5, 
                             'center_y': 0.5})
        layout.add_widget(background)
        
        info = Image(source="assets/img/home_screen/info.png", 
                     allow_stretch=True,
                     pos_hint={'center_x': 0.5, 
                               'center_y': 0.5})
        layout.add_widget(info)
        
        button_play = CustomButton(
            app=app,
            size_original=290,
            destination="choice_menu",
            source="assets/img/button/play.png",
            pos_hint={'center_x': 0.5, 
                      'center_y': 0.14},
        )
        layout.add_widget(button_play)
    
        self.add_widget(layout)
        