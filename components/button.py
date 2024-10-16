from kivy.uix.button import Button, ButtonBehavior
from kivy.graphics import Color, Ellipse
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.image import Image

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
    def __init__(self, app, destination: str, **kwargs):
        super(BackButton, self).__init__(**kwargs)
        self.app = app
        self.destination = destination
        
        self.default_size_hint = kwargs.get('size_hint', (0.5, 0.5))
        increased_size_hint = (self.default_size_hint[0] + 0.2, self.default_size_hint[1] + 0.2)    
        self.clicked_size_hint = increased_size_hint
        
        self.click_sound = SoundLoader.load('public/sound/click.mp3')
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.click_sound:
                self.click_sound.play()

            anim = Animation(size_hint=self.clicked_size_hint, duration=0.1)
            anim.start(self)

            Clock.schedule_once(self.change_screen_after_delay, 0.3)

        return super(BackButton, self).on_touch_down(touch) 

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            anim = Animation(size_hint=self.default_size_hint, duration=0.1)
            anim.start(self)

        return super(BackButton, self).on_touch_up(touch)  

    def change_screen_after_delay(self, dt):
        if self.destination == 'previous':
            self.app.back_screen()
        else:
            self.app.change_screen(self.destination)

        
class ButtonPlaying(Image):
    def __init__(self, app, **kwargs):
        super(ButtonPlaying, self).__init__(**kwargs)
        self.app = app
        
        self.default_size_hint = kwargs.get('size_hint', (0.5, 0.5))
        increased_size_hint = (self.default_size_hint[0] + 0.2, self.default_size_hint[1] + 0.2)    
        self.clicked_size_hint = increased_size_hint
        
        self.click_sound = SoundLoader.load('public/sound/click.mp3')
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.click_sound:
                self.click_sound.play()

            anim = Animation(size_hint=self.clicked_size_hint, duration=0.1)
            anim.start(self)

            Clock.schedule_once(self.change_screen_after_delay, 0.3)

        return super(ButtonPlaying, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            anim = Animation(size_hint=self.default_size_hint, duration=0.1)
            anim.start(self)

        return super(ButtonPlaying, self).on_touch_up(touch)

    def change_screen_after_delay(self, dt):
        self.app.change_screen('choice')
