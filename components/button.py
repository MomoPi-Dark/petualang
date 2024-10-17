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
        self.destination = destination  

        self.size_hint = (None, None)
        self._create_size(size_original)

        self.click_sound = SoundLoader.load('public/sound/click.mp3')

    def _create_size(self, size_original):
        original_width = self.texture_size[0]
        original_height = self.texture_size[1]
        target_width = size_original
        new_height = ((target_width / original_width) * original_height)
        self.original_size = (target_width, (new_height // 1))
        self.size = self.original_size
        self.increased_size = (self.original_size[0] * 2.0, self.original_size[1] * 2.0)
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.click_sound:
                self.click_sound.play()

            scale_up = Animation(size=self.increased_size, duration=0.2)
            scale_up.start(self)

            Clock.schedule_once(self.change_screen_after_delay, 0.3)

        return super(BackButton, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            scale_down = Animation(size=self.original_size, duration=0.2)
            scale_down.start(self)
        
        return super(BackButton, self).on_touch_up(touch)

    def change_screen_after_delay(self, dt):
        if self.destination == 'previous':
            self.app.back_screen() 
        else:
            self.app.change_screen(self.destination)
        
class ButtonPlaying(Image):
    def __init__(self, app, size_original, **kwargs):
        super(ButtonPlaying, self).__init__(**kwargs)
        self.app = app

        self.size_hint = (None, None)
        self._create_size(size_original)

        self.click_sound = SoundLoader.load('public/sound/click.mp3')
        
    def _create_size(self, size_original):
        original_width = self.texture_size[0]
        original_height = self.texture_size[1]
        target_width = size_original
        new_height = ((target_width / original_width) * original_height)
        self.original_size = (target_width, (new_height // 1))
        self.size = self.original_size
        self.increased_size = (self.original_size[0] * 2.0, self.original_size[1] * 2.0)    
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.click_sound:
                self.click_sound.play()

            scale_up = Animation(size=self.increased_size, duration=0.2)
            scale_up.start(self)

            Clock.schedule_once(self.change_screen_after_delay, 0.3)

        return super(ButtonPlaying, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            scale_down = Animation(size=self.original_size, duration=0.2)
            scale_down.start(self)
        
        return super(ButtonPlaying, self).on_touch_up(touch)

    def change_screen_after_delay(self, dt):
        self.app.change_screen('choice')
        