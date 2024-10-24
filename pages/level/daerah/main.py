from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.animation import Animation
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
            keep_ratio=True,
        )
        layout.add_widget(back_button)
        
        self.button_lvl_1 = CustomButton(
            app=app,
            size_original=250,
            destination="lagu_daerah_level_1",
            added_clicked_scale=0.02,
            source="assets/select_level/daerah/level_1.png",
            pos_hint={"x": 0.30, "top": 0.83},
            allow_stretch=True,
            keep_ratio=True
        )
        layout.add_widget(self.button_lvl_1)
        
        self.button_lvl_2 = CustomButton(
            app=app,
            size_original=250,
            destination="lagu_daerah_level_2",
            added_clicked_scale=0.02,
            source="assets/select_level/daerah/level_2.png",
            pos_hint={"x": 0.08, "top": 0.60},
            allow_stretch=True,
            keep_ratio=True
        )
        layout.add_widget(self.button_lvl_2)
        
        # self.button_lvl_3 = CustomButton(
        #     app=app,
        #     size_original=250,
        #     added_clicked_scale=0.02,
        #     source="assets/select_level/daerah/level_3.png",
        #     pos_hint={"x": 0.30, "top": 0.35},
        #     allow_stretch=True,
        #     keep_ratio=True
        # )
        # layout.add_widget(self.button_lvl_3)
        
        button_icon = CustomImage(
            added_clicked_scale=0.02,
            size_original=250,
            source="assets/select_level/daerah/icon.png",
            allow_stretch=True,
            keep_ratio=True,
        )
        layout.add_widget(button_icon)
        
        self.add_widget(layout)
        
    def on_enter(self):
        self.app.play_bg_sound()
        self.button_lvl_1.jiggle_effect()
        self.button_lvl_2.jiggle_effect()
        # self.button_lvl_3.jiggle_effect()