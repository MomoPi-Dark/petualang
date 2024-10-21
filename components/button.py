from kivy.graphics import Color
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Line

class CustomButton(Image):
    def __init__(self, app, size_original, destination="", sound_clicked="public/sound/click.mp3", show_border=False, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.app = app
        self.destination = destination
        self.show_border = show_border

        self.default_size_hint, self.clicked_size_hint, self.size_hint = self.create_size(size_original)

        self.click_sound = SoundLoader.load(sound_clicked)
        if self.click_sound:
            self.click_sound.bind(on_stop=self.change_screen_after_delay)

        self.scale_up = Animation(size_hint=self.clicked_size_hint, duration=0.2)
        self.scale_down = Animation(size_hint=self.default_size_hint, duration=0.2)

        if self.show_border:
            with self.canvas.before:
                Color(1, 0, 0, 1)
                self.border = Line(width=2)

            self.bind(pos=self._update_border, size=self._update_border)

    def _update_border(self, *args):
        self.border.rectangle = (self.x, self.y, self.width, self.height)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.click_sound:
                self.click_sound.play()

            self.scale_up.start(self)

        return super(CustomButton, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.scale_down.start(self)

        return super(CustomButton, self).on_touch_up(touch)

    def change_screen_after_delay(self, *args):
        self.scale_up.stop(self)
        self.scale_down.stop(self)

        self._delayed_screen_change()

    def _delayed_screen_change(self):
        if self.destination == "":
            return

        if self.destination == 'previous':
            self.app.back_screen()
        else:
            self.app.change_screen(self.destination)

    def create_size(self, size_original):
        original_width = self.texture_size[0]
        original_height = self.texture_size[1]

        target_width = size_original
        new_height = (target_width / original_width) * original_height

        window_width = Window.size[0]
        window_height = Window.size[1]

        default_size_hint = (target_width / window_width, new_height / window_height)
        clicked_size_hint = (default_size_hint[0] + 0.1, default_size_hint[1] + 0.1)

        default_hint = default_size_hint

        return default_size_hint, clicked_size_hint, default_hint

class ImageWithBorder(Image):
    def __init__(self, **kwargs):
        super(ImageWithBorder, self).__init__(**kwargs)

        with self.canvas.before:
            Color(1, 0, 0, 1) 
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=2)

        self.bind(pos=self.update_border, size=self.update_border)

    def update_border(self, *args):
        self.border.rectangle = (self.x, self.y, self.width, self.height)
