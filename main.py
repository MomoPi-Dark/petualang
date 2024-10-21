import sys

from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.core.text import LabelBase

from pages.level.daerah.main import LevelDaerah
from pages.level.kemerdekaan.main import LevelKemerdekaan
from pages.main_menu import MainMenuScreen
from pages.level.select_level_menu import ChooseGameScreen

Window.size = (480, 800)

LabelBase.register(name='lazy_dog', fn_regular='public/font/lazy_dog.ttf')
LabelBase.register(name='satoshi', fn_regular='public/font/satoshi.ttf')
LabelBase.register(name='more_sugar', fn_regular='public/font/more_sugar.ttf')

class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.title = "Nada Petualang Cilik"
        self.icon = "public/img/icon.png"
        
        self.background_sound = SoundLoader.load("public/sound/bg1.mp3")
        if self.background_sound:
            self.background_sound.loop = True
            self.background_sound.volume = 0.5
            self.background_sound.play()

    def build(self):
        self.screen_manager = ScreenManager(transition=FadeTransition(duration=0.5), size_hint=(1, 1))
        
        # Main menu
        self.screen_manager.add_widget(MainMenuScreen(name='menu', app=self))
        self.screen_manager.add_widget(ChooseGameScreen(name='choice_menu', app=self))
        
        # Level Select
        
        # Level Select kemerdakaan
        self.screen_manager.add_widget(LevelKemerdekaan(name='lagu_kemerdekaan', app=self))
        # self.screen_manager.add_widget(LevelDaerah(name='lagu_daerah_lvl1', app=self))
        # self.screen_manager.add_widget(LevelDaerah(name='lagu_daerah_lvl2', app=self))
        # self.screen_manager.add_widget(LevelDaerah(name='lagu_daerah_lvl3', app=self))
        
        # Level Select lagu daerah
        self.screen_manager.add_widget(LevelDaerah(name='lagu_daerah', app=self))
        # self.screen_manager.add_widget(LevelDaerah(name='lagu_daerah_lvl1', app=self))
        # self.screen_manager.add_widget(LevelDaerah(name='lagu_daerah_lvl2', app=self))
        # self.screen_manager.add_widget(LevelDaerah(name='lagu_daerah_lvl3', app=self))
        
        return self.screen_manager

    def back_screen(self):
        self.screen_manager.current = self.screen_manager.previous()
    
    def change_screen(self, screen_name):
        self.screen_manager.current = screen_name
    
if __name__ == "__main__":
    try:
        MyApp().run()
    except KeyboardInterrupt:
        sys.exit(0)