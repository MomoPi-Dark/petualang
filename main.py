import sys

from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.core.text import LabelBase
from kivy.config import Config
from kivy.clock import Clock

from pages.level.daerah.level_1 import Daerah_Level_1
from pages.level.daerah.level_2 import Daerah_Level_2
from pages.level.daerah.main import LevelDaerah
from pages.level.kemerdekaan.level_1 import Kemerdekaan_Level_1
from pages.level.kemerdekaan.level_2 import Kemerdekaan_Level_2
from pages.level.kemerdekaan.main import LevelKemerdekaan
from pages.level.select_level_menu import ChooseGameScreen
from pages.main_menu import MainMenuScreen

Window.size = (480, 800)

LabelBase.register(name='lazy_dog', fn_regular='assets/font/lazy_dog.ttf')
LabelBase.register(name='satoshi', fn_regular='assets/font/satoshi.ttf')
LabelBase.register(name='more_sugar', fn_regular='assets/font/more_sugar.ttf')

Config.set('graphics', 'scroll_thumb_image', 'assets/img/icons/heart.png')

class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.title = "Nada Petualang Cilik"
        self.icon = "assets/img/icon.png"
        
        self.background_sound = SoundLoader.load("assets/sfx/bgm.mp3")
        
        self._fade_out_interval = 0.1  
        self._fade_out_rate = 0.05   
        self._fade_in_rate = 0.05     
        self._max_volume = 0.5 
        
        self.play_bg_sound()

    def build(self):
        self.screen_manager = ScreenManager(transition=FadeTransition(duration=0.5), size_hint=(1, 1))
        
        # Main menu
        self.screen_manager.add_widget(MainMenuScreen(name='menu', app=self))
        self.screen_manager.add_widget(ChooseGameScreen(name='choice_menu', app=self))
        
        # Level Select
        
        # Level Select kemerdakaan
        self.screen_manager.add_widget(LevelKemerdekaan(name='lagu_kemerdekaan', app=self))
        self.screen_manager.add_widget(Kemerdekaan_Level_1(name='lagu_kemerdekaan_level_1', app=self))
        self.screen_manager.add_widget(Kemerdekaan_Level_2(name='lagu_kemerdekaan_level_2', app=self))
        
        # Level Select lagu daerah
        self.screen_manager.add_widget(LevelDaerah(name='lagu_daerah', app=self))
        self.screen_manager.add_widget(Daerah_Level_1(name='lagu_daerah_level_1', app=self))
        self.screen_manager.add_widget(Daerah_Level_2(name='lagu_daerah_level_2', app=self))
        
        return self.screen_manager

    def back_screen(self):
        self.screen_manager.current = self.screen_manager.previous()
    
    def change_screen(self, screen_name):
        self.screen_manager.current = screen_name
    
    def stop_bg_sound(self, force=False):
        if self.background_sound:
            if force:
                self.background_sound.stop()
            else:
                Clock.schedule_interval(self._fade_out_volume, self._fade_out_interval)
            
    def _fade_out_volume(self, dt):
        current_volume = self.background_sound.volume
        if current_volume > 0:
            new_volume = max(0, current_volume - self._fade_out_rate)    
            self.background_sound.volume = new_volume
        else:
            self.background_sound.stop()
            return False 
        
    def play_bg_sound(self):
        if self.background_sound:
            if not self.background_sound.state == 'play':
                self.background_sound.loop = True
                self.background_sound.volume = 0.5
                self.background_sound.play()
                
                Clock.schedule_interval(self._fade_in_volume, self._fade_out_interval)
    def _fade_in_volume(self, dt):
        current_volume = self.background_sound.volume
        if current_volume < self._max_volume:
            new_volume = min(self._max_volume, current_volume + self._fade_in_rate) 
            self.background_sound.volume = new_volume
        else:
            return False 
        
if __name__ == "__main__":
    try:
        MyApp().run()
    except KeyboardInterrupt:
        sys.exit(0)