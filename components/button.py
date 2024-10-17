from typing import Any
from kivy.uix.button import Button, ButtonBehavior
from kivy.graphics import Color, Ellipse
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.core.window import Window

class OvalButton(Button):
    def __init__(self, click_sound, **kwargs):
        super(OvalButton, self).__init__(**kwargs)
        self.click_sound = click_sound

        with self.canvas.before:
            Color(*self.background_color)
            self.oval = Ellipse(size=self.size, pos=self.pos)

        self.bind(size=self._update_oval, pos=self._update_oval)

    def _update_oval(self, *args):
        self.oval.pos = self.pos
        self.oval.size = self.size

    def on_press(self):
        if self.click_sound:
            self.click_sound.play()


class BackButton(Image):
    def __init__(self, app, size_original, destination='previous', **kwargs):
        super(BackButton, self).__init__(**kwargs)
        self.app = app
        
        self.click_sound = SoundLoader.load('public/sound/click.mp3')
        self.destination = destination  

        self.default_size_hint, self.clicked_size_hint, self.size_hint = _create_size(self.texture_size, size_original)
        
        self.scale_up = Animation(size_hint=self.clicked_size_hint, duration=0.2)
        self.scale_down = Animation(size_hint=self.default_size_hint, duration=0.2)
        
        self.scale_down.bind(on_complete=lambda *args: self.change_screen_after_delay())

    def on_touch_down(self, touch):
        if self.click_sound:
            self.click_sound.play()
        self.scale_up.start(self)
            
        return super(BackButton, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        self.scale_down.start(self)
        return super(BackButton, self).on_touch_up(touch)

    def change_screen_after_delay(self):
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
        
        self.scale_up = Animation(size_hint=self.clicked_size_hint, duration=0.2)
        self.scale_down = Animation(size_hint=self.default_size_hint, duration=0.2)
        
        self.scale_down.bind(on_complete=lambda *args: self.change_screen_after_delay())

    def on_touch_down(self, touch):
        if self.click_sound:
            self.click_sound.play()
        self.scale_up.start(self)
            
        return super(ButtonPlaying, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        self.scale_down.start(self)
        return super(ButtonPlaying, self).on_touch_up(touch)

    def change_screen_after_delay(self):
        self.app.change_screen('choice')
        
def _create_size(texture_size: Any | list[int], size_original):
        target_width = size_original
        original_width = texture_size[0]
        original_height = texture_size[1]
        new_height = (target_width / original_width) * original_height
        
        window_width = Window.size[0]
        window_height = Window.size[1]
        
        default_size_hint = (target_width / window_width, new_height / window_height)
        size_hint = default_size_hint
        
        clicked_size_hint = (default_size_hint[0] + 0.12, default_size_hint[1] + 0.12) 
        
        return default_size_hint, clicked_size_hint, size_hint  