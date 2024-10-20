from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from components.button import CustomButton

class ChooseIcon(FloatLayout):
    def __init__(self, app, **kwargs):
        super(ChooseIcon, self).__init__(**kwargs)
        self.app = app
        
        centerY = 0.40

        lagu_daerah_label = Label(
            text="Lagu\nDaerah",
            font_name="more_sugar",
            color=(213/255, 77/255, 55/255, 1), 
            font_size=30,
            pos_hint={'center_x': 0.25, 'center_y': 0.60},
            halign='center',
            valign='middle' 
        )
        lagu_daerah_label.bind(size=lagu_daerah_label.setter('text_size'))
        lagu_daerah = CustomButton(
            app=app,
            size_original=190,
            destination="lagu_daerah",
            pos_hint={'center_x': 0.25, 'center_y': centerY},
            source="public/img/v2/choice_menu_screen/lagu_daerah.png",
            allow_stretch=True,
            keep_ratio=True
        )
        self.add_widget(lagu_daerah_label)
        self.add_widget(lagu_daerah)

        lagu_nasional_label = Label(
            text="Lagu\nKemerdekaan",
            font_name="more_sugar",
            color=(213/255, 77/255, 55/255, 1),
            font_size=30,
            pos_hint={'center_x': 0.75, 'center_y': 0.60},
            halign='center',
            valign='middle'
        )
        lagu_nasional_label.bind(size=lagu_nasional_label.setter('text_size'))  # Ensure text is centered
        lagu_nasional = CustomButton(
            app=app,
            size_original=200,
            destination="lagu_kemerdekaan",
            pos_hint={'center_x': 0.75, 'center_y': centerY},
            source="public/img/v2/choice_menu_screen/lagu_kebangsaan.png",
            allow_stretch=True,
            keep_ratio=True
        )
        self.add_widget(lagu_nasional_label)
        self.add_widget(lagu_nasional)
        
class ChooseGameScreen(Screen):
    def __init__(self, app, **kwargs):
        super(ChooseGameScreen, self).__init__(**kwargs)
        self.app = app
        
        layout = FloatLayout()
        
        background = Image(source="public/img/v2/choice_menu_screen/bg1.png",
                            allow_stretch=True,
                            keep_ratio=True)
        layout.add_widget(background)
        
        singers_image = Image(source="public/img/v2/choice_menu_screen/singers.png",
                              size_hint=(0.4, 0.4),
                              pos_hint={'center_x': 0.5, 'center_y': 0.80},
                              allow_stretch=True,
                              keep_ratio=True)
        layout.add_widget(singers_image)
        
        grid_layout_button = GridLayout(cols=2, rows=2, spacing=10, pos_hint={'center_x': 0.5})
        
        choose_icon = ChooseIcon(app=app)
        grid_layout_button.add_widget(choose_icon)
        
        layout.add_widget(grid_layout_button)
        
        back_button = CustomButton(
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
        
        
        