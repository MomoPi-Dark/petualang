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

        center_y = 0.35
        label_center_y = center_y + 0.20

        color = (213/255, 77/255, 55/255, 1)

        lagu_daerah_label = Label(
            text="Lagu\nDaerah",
            font_name="more_sugar",
            color=color, 
            font_size=33,
            pos_hint={'center_x': 0.25, 'center_y': label_center_y},
            halign='center',
            valign='middle' 
        )
        lagu_daerah_label.bind(size=lagu_daerah_label.setter('text_size'))
        lagu_daerah = CustomButton(
            app=app,
            size_original=200,
            destination="lagu_daerah",
            pos_hint={'center_x': 0.25, 'center_y': center_y},
            source="assets/img/choice_menu_screen/lagu_daerah.png",
            allow_stretch=True,
            keep_ratio=True
        )
        self.add_widget(lagu_daerah_label)
        self.add_widget(lagu_daerah)

        lagu_nasional_label = Label(
            text="Lagu\nKemerdekaan",
            font_name="more_sugar",
            color=color,
            font_size=33,
            pos_hint={'center_x': 0.75, 'center_y': label_center_y},
            halign='center',
            valign='middle'
        )
        lagu_nasional_label.bind(size=lagu_nasional_label.setter('text_size'))
        lagu_nasional = CustomButton(
            app=app,
            size_original=200,
            destination="lagu_kemerdekaan",
            pos_hint={'center_x': 0.75, 'center_y': center_y},
            source="assets/img/choice_menu_screen/lagu_kebangsaan.png",
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
        
        background = Image(source="assets/img/bg.png",
                            allow_stretch=True,
                            keep_ratio=True)
        layout.add_widget(background)
        
        singers_image = Image(source="assets/img/choice_menu_screen/singers.png",
                              size_hint=(0.45, 0.45),
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
            size_original=60,
            added_clicked_scale=0.02,
            destination="menu",
            source="assets/img/button/arrow_3.png",
            pos_hint={"x": 0.83, "top": 0.98},
            allow_stretch=True,
            keep_ratio=True
        )
        layout.add_widget(back_button)
        
        self.add_widget(layout)
        
        
        