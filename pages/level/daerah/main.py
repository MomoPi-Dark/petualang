from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

from components.button import CustomButton, CustomImage

class LevelDaerah(Screen):
    def __init__(self, app, **kwargs):
        super(LevelDaerah, self).__init__(**kwargs)
        self.app = app
        
        layout = FloatLayout()
        
        background = Image(source="assets/img/home_screen/bg.png", 
                   size_hint=(1, 1), 
                   pos_hint={'center_x': 0.5, 
                             'center_y': 0.5})
        layout.add_widget(background)
        
        back_button = CustomButton(
            app=app,
            size_original=60,
            added_clicked_scale=0.02,
            destination="choice_menu",
            source="assets/img/button/arrow_3.png",
            pos_hint={"x": 0.83, "top": 0.98},
            allow_stretch=True,
            keep_ratio=True
        )
        layout.add_widget(back_button)
        
        button_lvl_1 = CustomButton(
            app=app,
            size_original=250,
            added_clicked_scale=0.02,
            source="assets/img/level/daerah/level_1.png",
            pos_hint={"x": 0.43, "top": 0.83},
            allow_stretch=True,
            keep_ratio=True
        )
        layout.add_widget(button_lvl_1)
        
        button_lvl_2 = CustomButton(
            app=app,
            size_original=250,
            added_clicked_scale=0.02,
            source="assets/img/level/daerah/level_2.png",
            pos_hint={"x": 0.08, "top": 0.58},
            allow_stretch=True,
            keep_ratio=True
        )
        layout.add_widget(button_lvl_2)
        
        button_lvl_3 = CustomButton(
            app=app,
            size_original=250,
            added_clicked_scale=0.02,
            source="assets/img/level/daerah/level_3.png",
            pos_hint={"x": 0.43, "top": 0.35},
            allow_stretch=True,
            keep_ratio=True
        )
        layout.add_widget(button_lvl_3)
        
        button_icon = CustomImage(
            added_clicked_scale=0.02,
            size_original=250,
            source="assets/img/level/daerah/icon.png",
            allow_stretch=True,
            keep_ratio=True,
        )
        layout.add_widget(button_icon)
        
        self.add_widget(layout)
        