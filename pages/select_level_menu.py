from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

from components.button import BackButton

class ChooseGameScreen(Screen):
    def __init__(self, app, **kwargs):
        super(ChooseGameScreen, self).__init__(**kwargs)
        self.app = app
        
        layout = FloatLayout()
        
        background = Image(source="public/img/v2/choice_screen/bg1.png",
                            allow_stretch=True,
                            keep_ratio=True)
        layout.add_widget(background)
        
        back_button = BackButton(
            app=app,
            size_original=280,
            destination="previous",
            source="public/img/v2/button/back.png",
            pos_hint={'center_x': 0.5, 'center_y': 0.11},
            allow_stretch=True,
            keep_ratio=True
        )
        layout.add_widget(back_button)
        
        self.add_widget(layout)
        