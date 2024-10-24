from kivy.graphics import Color
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Line

class CustomImage(Image):
    def __init__(self, size_original, added_clicked_scale = 0.1, **kwargs):
        super(CustomImage, self).__init__(**kwargs)
        
        self.default_size_hint, self.clicked_size_hint, self.size_hint = self.create_size(size_original, added_clicked_scale)

    def create_size(self, size_original, added_clicked_scale=0.1):
        original_width = self.texture_size[0]
        original_height = self.texture_size[1]

        target_width = size_original
        new_height = (target_width / original_width) * original_height

        window_width = Window.size[0]
        window_height = Window.size[1]

        default_size_hint = (target_width / window_width, new_height / window_height)
        clicked_size_hint = (default_size_hint[0] + added_clicked_scale, default_size_hint[1] + added_clicked_scale)

        default_hint = default_size_hint

        return default_size_hint, clicked_size_hint, default_hint

class CustomButton(Image):
    def __init__(self, app, size_original, destination="", sound_clicked="assets/sfx/click.mp3", show_border=False, added_clicked_scale=0.1, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.app = app
        self.destination = destination
        self.show_border = show_border
        self.disabled = False

        self.default_size_hint, self.clicked_size_hint, self.size_hint = self._create_size(size_original, added_clicked_scale)

        self.click_sound = None
        if sound_clicked != "":
            self.click_sound = SoundLoader.load(sound_clicked)
            if self.click_sound:
                self.click_sound.bind(on_stop=self._play_animation_and_change_screen)

        self.scale_up = Animation(size_hint=self.clicked_size_hint, duration=0.2)
        self.scale_down = Animation(size_hint=self.default_size_hint, duration=0.2)

        self.scale_down.bind(on_complete=self._delayed_screen_change)

        if self.show_border:
            with self.canvas.before:
                Color(1, 0, 0, 1)
                self.border = Line(width=2)

            self.bind(pos=self._update_border, size=self._update_border)

        self.register_event_type('on_touch')

    def _update_border(self, *args):
        self.border.rectangle = (self.x, self.y, self.width, self.height)

    def on_touch(self, touch):
        return touch

    def on_touch_down(self, touch):
        if self.disabled:
            return False

        if self.collide_point(*touch.pos):
            if self.click_sound:
                self.click_sound.play()

            self.scale_up.start(self)
            self.dispatch("on_touch", touch)

        return super(CustomButton, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.scale_down.start(self)

        return super(CustomButton, self).on_touch_up(touch)

    def _play_animation_and_change_screen(self, *args):
        self.scale_down.start(self)

    def _delayed_screen_change(self, *args):
        if self.destination == "":
            return

        if self.destination == 'previous':
            self.app.back_screen()
        else:
            self.app.change_screen(self.destination)

    def _create_size(self, size_original, added_clicked_scale=0.1):
        original_width = self.texture_size[0]
        original_height = self.texture_size[1]

        target_width = size_original
        new_height = (target_width / original_width) * original_height

        window_width = Window.size[0]
        window_height = Window.size[1]

        default_size_hint = (target_width / window_width, new_height / window_height)
        clicked_size_hint = (default_size_hint[0] + added_clicked_scale, default_size_hint[1] + added_clicked_scale)

        return default_size_hint, clicked_size_hint, default_size_hint

    def jiggle_effect(self):
        anim = Animation(pos_hint={'x': self.pos_hint['x'] + 0.01, 'y': self.pos_hint.get('y', 0.5)}, duration=0.1) + \
               Animation(pos_hint={'x': self.pos_hint['x'] - 0.01, 'y': self.pos_hint.get('y', 0.5)}, duration=0.1)
        anim.start(self)

    def set_disable(self, disable: bool):
        self.disabled = disable
        if disable:
            self.color = (0.5, 0.5, 0.5, 1)
        else:
            self.color = (1, 1, 1, 1)
            
        self.set_disabled(disable)


class ImageWithBorder(Image):
    def __init__(self, **kwargs):
        super(ImageWithBorder, self).__init__(**kwargs)

        with self.canvas.before:
            Color(1, 0, 0, 1) 
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=2)

        self.bind(pos=self.update_border, size=self.update_border)

    def update_border(self, *args):
        self.border.rectangle = (self.x, self.y, self.width, self.height)
