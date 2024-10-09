from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.core.text import LabelBase
from kivy.graphics import Ellipse, Color

Window.size = (800, 480)

LabelBase.register(name="moreSugar", fn_regular="moreSugar.ttf")


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


class LevelSelection(FloatLayout):
    def __init__(self, app, **kwargs):
        super(LevelSelection, self).__init__(**kwargs)
        self.app = app

        self.bg_image = Image(source="bgLevel.png")
        self.add_widget(self.bg_image)

        level1_button = OvalButton(
            click_sound=SoundLoader.load("buttonClick.mp3"),
            text="Level 1",
            font_size="30sp",
            font_name="moreSugar",
            background_normal="",
            background_color=(0.6, 0.3, 0.2, 1),
            color=(0.6, 0.8, 0.4, 1),
            size_hint=(0.5, 0.15),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        self.add_widget(level1_button)

        back_button = OvalButton(
            click_sound=SoundLoader.load("buttonClick.mp3"),
            text="Back",
            font_size="30sp",
            font_name="moreSugar",
            background_normal="",
            background_color=(0.6, 0.3, 0.2, 1),
            color=(0.6, 0.8, 0.4, 1),
            size_hint=(0.5, 0.15),
            pos_hint={"center_x": 0.5, "center_y": 0.3},
        )
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

        self.mute_image = Image(
            source="musikOn.png",
            size_hint=(0.1, 0.1),
            pos_hint={"x": 0.05, "top": 0.95},
        )
        self.mute_image.bind(on_touch_down=self.toggle_sound)
        self.add_widget(self.mute_image)

    def toggle_sound(self, instance, touch):
        if self.app.background_sound.state == "play":
            self.app.background_sound.stop()
            self.mute_image.source = "mute.png"
        else:
            self.app.background_sound.play()
            self.mute_image.source = "musikOn.png"
        self.mute_image.reload()

    def go_back(self, instance):
        self.app.change_screen(MainMenu(self.app))


class MainMenu(FloatLayout):
    def __init__(self, app, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.app = app

        self.bg_image = Image(source="bgAwal.png")
        self.add_widget(self.bg_image)

        click_sound = SoundLoader.load("buttonClick.mp3")

        self.start_button = OvalButton(
            click_sound=click_sound,
            text="Mulai Game",
            font_size="30sp",
            font_name="moreSugar",
            background_normal="",
            background_color=(0.6, 0.3, 0.2, 1),
            color=(0.6, 0.8, 0.4, 1),
            size_hint=(0.5, 0.15),
            pos_hint={"center_x": 0.5, "center_y": 0.4},
        )
        self.start_button.bind(on_press=self.start_game)
        self.add_widget(self.start_button)

        self.exit_button = OvalButton(
            click_sound=click_sound,
            text="Keluar Game",
            font_size="30sp",
            font_name="moreSugar",
            background_normal="",
            background_color=(0.6, 0.3, 0.2, 1),
            color=(0.6, 0.8, 0.4, 1),
            size_hint=(0.5, 0.15),
            pos_hint={"center_x": 0.5, "center_y": 0.2},
        )
        self.exit_button.bind(on_press=self.exit_game)
        self.add_widget(self.exit_button)

        self.mute_image = Image(
            source="musikOn.png",
            size_hint=(0.1, 0.1),
            pos_hint={"x": 0.05, "top": 0.95},
        )
        self.mute_image.bind(on_touch_down=self.toggle_sound)
        self.add_widget(self.mute_image)

    def toggle_sound(self, instance, touch):
        if self.app.background_sound.state == "play":
            self.app.background_sound.stop()
            self.mute_image.source = "mute.png"
        else:
            self.app.background_sound.play()
            self.mute_image.source = "musikOn.png"
        self.mute_image.reload()

    def start_game(self, instance):
        print("Mulai Game diklik!")
        self.app.change_screen(LevelSelection(self.app))

    def exit_game(self, instance):
        App.get_running_app().stop()


class MyGameApp(App):
    def __init__(self, **kwargs):
        super(MyGameApp, self).__init__(**kwargs)
        self.background_sound = SoundLoader.load("musik.mp3")
        if self.background_sound:
            self.background_sound.loop = True
            self.background_sound.play()

    def build(self):
        return MainMenu(self)

    def change_screen(self, new_screen):
        self.root.clear_widgets()
        self.root.add_widget(new_screen)


if __name__ == "_main_":
    MyGameApp().run()
