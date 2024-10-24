from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty

from components.button import CustomButton, CustomImage

class LayoutQuest(FloatLayout):
    on_value_submit = ObjectProperty()

    def __init__(self, app, descriptions: list[str], bg: str, result: str, button_title: str, btn_a_src: str, btn_b_src: str, btn_c_src: str, bg_sound: str = "", **kwargs):
        super(LayoutQuest, self).__init__(**kwargs)
        
        self.app = app
        self._jawaban = result
        self.already_answered = False

        background = Image(source=bg, 
                           size_hint=(1.1, 1.1), 
                           pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(background)

        title = CustomImage(source=button_title,
                            size_original=400,
                            pos_hint={'center_x': 0.5, 'center_y': 0.85})
        self.add_widget(title)
        
        y_for_scroll = 0.57
        
        bg_lyric = CustomImage(
                size_original=450,
                source="assets/quest/bg_lyric.png",
                pos_hint={'center_x': 0.5, 'center_y': y_for_scroll})
        self.add_widget(bg_lyric)
        
        scrollview = ScrollView(size_hint=(None, None), 
                                size=(400, 200), 
                                do_scroll_x=False, 
                                do_scroll_y=True,
                                bar_width=10,
                                scroll_type=['bars', 'content'],
                                bar_inactive_color=(0.835, 0.302, 0.216, 1),  
                                bar_color=(0.835, 0.302, 0.216, 1),
                                pos_hint={'center_x': 0.5, 'center_y': y_for_scroll})

        layout_grid = GridLayout(cols=1, 
                                 padding=[10, 10, 20, 10],
                                 spacing=10, 
                                 size_hint_y=None)
        layout_grid.bind(minimum_height=layout_grid.setter('height'))

        for i in range(len(descriptions)):
            label = Label(text=f"{descriptions[i]}", 
                          size_hint_y=None, 
                          height=30, 
                          font_size='20sp', 
                          color=(213/255, 77/255, 55/255, 1), 
                          font_name="more_sugar")
            layout_grid.add_widget(label)

        scrollview.add_widget(layout_grid)
        self.add_widget(scrollview)

        self.b1 = CustomButton(app=app, 
                          source=btn_a_src, 
                          sound_clicked="",
                          size_original=380,
                          pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.b2 = CustomButton(app=app, 
                          source=btn_b_src, 
                          sound_clicked="",
                          size_original=380,
                          pos_hint={'center_x': 0.5, 'center_y': 0.2})
        self.b3 = CustomButton(app=app, 
                          source=btn_c_src, 
                          sound_clicked="",
                          size_original=380,
                          pos_hint={'center_x': 0.5, 'center_y': 0.1})

        self.add_widget(self.b1)
        self.b1.bind(on_touch=lambda instance, touch: self._on_value("a"))
        
        self.add_widget(self.b2)
        self.b2.bind(on_touch=lambda instance, touch: self._on_value("b"))
        
        self.add_widget(self.b3)
        self.b3.bind(on_touch=lambda instance, touch: self._on_value("c"))
        
        self.wrong_sound = SoundLoader.load("assets/sfx/fail.mp3")
        self.correct_sound = SoundLoader.load("assets/sfx/correct.mp3")
        
        self.register_event_type('on_value_submit')
        
        self.bg_sound = SoundLoader.load(bg_sound)
        
        self._set_disable_button(True)
        
        
    def _set_disable_button(self, disable: bool):
        self.b1.set_disable(disable)
        self.b2.set_disable(disable)
        self.b3.set_disable(disable)
    
    def _on_value(self, value):
        if self.already_answered:
            return
        
        self.already_answered = True
        
        is_correct = False
        if self._jawaban.lower() == value:
            is_correct = True
            self.correct_sound.play()
        else:
            self.wrong_sound.play()
        self._set_disable_button(True)
        
        self.dispatch('on_value_submit', is_correct, value)
        
    def on_value_submit(self, is_correct, value):
        return True
    
    def call_screen(self):
        self.app.stop_bg_sound()
        
        if self.bg_sound:
            self.bg_sound.volume = 0.5
            self.bg_sound.play()
            self.bg_sound.bind(on_stop=lambda insance: self._set_disable_button(False))
        else:
            self._set_disable_button(False)
    
class LayoutFinish(FloatLayout):
    def __init__(self, app, point_quest: dict, destination: str, **kwargs):
        super(LayoutFinish, self).__init__(**kwargs)
        
        self.app = app
        self.point_quest = point_quest
        
        background = Image(source="assets/img/bg.png", 
                           size_hint=(1.1, 1.1), 
                           pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(background)
        
        icon = CustomImage(source="assets/img/icon.png",
                            size_original=240,
                            pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.add_widget(icon)
        
        finish_box = CustomImage(source="assets/quest/finish/finish_box.png",
                                 size_original=400,
                                 pos_hint={'center_x': 0.5, 'center_y': 0.48})
        self.add_widget(finish_box)
        
        self.point = 0
        for _, value in point_quest.items():
            self.point += value
        
        label = Label(text=f"Score",
                      size_hint=(None, None),
                      pos_hint={'center_x': 0.5, 'center_y': 0.57},
                      font_size='50sp',
                      color=(213/255, 77/255, 55/255, 1),
                      halign='center',
                      valign='middle', 
                      font_name="more_sugar")
        self.add_widget(label)
        
        label_score = Label(text=f"{self.point}",
                      size_hint=(None, None),
                      pos_hint={'center_x': 0.5, 'center_y': 0.47},
                      font_size='50sp',
                      color=(213/255, 77/255, 55/255, 1),
                      halign='center',
                      valign='middle', 
                      font_name="more_sugar")
        self.add_widget(label_score)
        
        button_main_menu = CustomButton(app=app,
                                        source="assets/quest/finish/main_menu.png",
                                        size_original=290,
                                        destination=destination,
                                        pos_hint={'center_x': 0.5, 'center_y': 0.25})
        self.add_widget(button_main_menu)
        
        self.bg_sound = SoundLoader.load("assets/sfx/finish.mp3")
        
        if self.bg_sound:
            self.bg_sound.volume = 1
            self.bg_sound.play()
        
        