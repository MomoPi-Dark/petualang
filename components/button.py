from typing import Any
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line

class BackButton(Image):
    def __init__(self, app, size_original, destination='previous', **kwargs):
        super(BackButton, self).__init__(**kwargs)
        self.app = app
        
        self.destination = destination  

        self.default_size_hint, self.clicked_size_hint, self.size_hint = _create_size(self.texture_size, size_original)
        
        self.click_sound = SoundLoader.load('public/sound/click.mp3')
        if self.click_sound:
            self.click_sound.bind(on_stop=self.change_screen_after_delay)
        
        self.scale_up = Animation(size_hint=self.clicked_size_hint, duration=0.2)
        self.scale_down = Animation(size_hint=self.default_size_hint, duration=0.2)
        
    def on_touch_down(self, touch):
        if self.click_sound:
            self.click_sound.play()
        self.scale_up.start(self)
            
        return super(BackButton, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        self.scale_down.start(self)
        return super(BackButton, self).on_touch_up(touch)
    
    def change_screen_after_delay(self, *args):
        self.scale_up.stop(self) 
        self.scale_down.stop(self)
        
        Clock.schedule_once(self._delayed_screen_change, 0.1)
        
    def _delayed_screen_change(self, dt):
        if self.destination == 'previous':
            self.app.back_screen() 
        else:
            self.app.change_screen(self.destination)

class ButtonPlaying(Image):
    def __init__(self, app, size_original, **kwargs):
        super(ButtonPlaying, self).__init__(**kwargs)
        self.app = app

        self.default_size_hint, self.clicked_size_hint, self.size_hint = _create_size(self.texture_size, size_original)
        
        self.click_sound = SoundLoader.load('public/sound/click.mp3')
        if self.click_sound:
            self.click_sound.bind(on_stop=self.change_screen_after_delay)  # Bind on_stop to change screen
        
        self.scale_up = Animation(size_hint=self.clicked_size_hint, duration=0.2)
        self.scale_down = Animation(size_hint=self.default_size_hint, duration=0.2)
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.click_sound:
                self.click_sound.play()

            self.scale_up.start(self)
            
        return super(ButtonPlaying, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.scale_down.start(self)

        return super(ButtonPlaying, self).on_touch_up(touch)

    def change_screen_after_delay(self, *args):
        self.scale_up.stop(self) 
        self.scale_down.stop(self)
        
        Clock.schedule_once(self._delayed_screen_change, 0.1)
        
    def _delayed_screen_change(self, dt):
        self.app.change_screen('choice')
        
def _create_size(texture_size: list[int], size_original):
    target_width = size_original
    original_width = texture_size[0]
    original_height = texture_size[1]
    
    new_height = (target_width / original_width) * original_height
    
    window_width = Window.size[0]
    window_height = Window.size[1]
    
    default_size_hint = (target_width / window_width, new_height / window_height)
    
    clicked_size_hint = (default_size_hint[0] + 0.12, default_size_hint[1] + 0.12)
    
    return default_size_hint, clicked_size_hint, default_size_hint

class ImageWithBorder(Image):
    def __init__(self, **kwargs):
        super(ImageWithBorder, self).__init__(**kwargs)

        with self.canvas.before:
            Color(1, 0, 0, 1) 
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=2)

        self.bind(pos=self.update_border, size=self.update_border)

    def update_border(self, *args):
        self.border.rectangle = (self.x, self.y, self.width, self.height)
