import sys
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Window.size = (480, 800)


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


class CustomButton(Button):
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)

        self.size_hint = (
            0.2,
            0.3,
        )
        self.pos_hint = {"center_x": 0.5, "center_y": 0.38}

        with self.canvas.before:
            Color(57 / 255, 171 / 255, 231 / 255, 1)  # Blue background
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def _update_text_size(self, *args):
        self.label.text_size = self.label.size


class ChooseGame(FloatLayout):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        with self.canvas.before:
            Color(57 / 255, 171 / 255, 231 / 255, 1)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        self.back_button = Image(
            source="public/img/back.png",
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={"x": 0.05, "top": 0.95},
        )
        self.back_button.bind(on_touch_down=self.back_to_main_menu)
        self.add_widget(self.back_button)

        self.middle_image = Image(
            source="public/img/burung.png",
            pos_hint={
                "center_x": 0.5,
                "top": 1.03,
            },
            size_hint=(0.6, 0.6),
        )
        self.add_widget(self.middle_image)

        # Create a BoxLayout to arrange buttons side by side
        layout = BoxLayout(orientation="horizontal", spacing=20, padding=20)

        self.game_lagu_kebangasaan = CustomButton(
            text="Lagu\nKebangasaan",
            font_size="24px",
            font_name="public/font/satoshi.ttf",
            background_color=(57 / 255, 171 / 255, 231 / 255, 1),
        )
        self.game_lagu_kebangasaan.bind(on_press=self.lagu_kebangsaan)

        self.game_lagu_daerah = CustomButton(
            text="Lagu Daerah",
            font_size="24px",
            font_name="public/font/satoshi.ttf",
            background_color=(57 / 255, 171 / 255, 231 / 255, 1),
        )
        self.game_lagu_daerah.bind(on_press=self.lagu_daerah)

        # Add the buttons to the horizontal layout
        layout.add_widget(self.game_lagu_kebangasaan)
        layout.add_widget(self.game_lagu_daerah)

        # Add the horizontal layout to the main layout (assuming it's added somewhere in your app)
        self.add_widget(layout)

    def _update_rect(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def back_to_main_menu(self, instance, touch):
        click_sound = SoundLoader.load("public/sound/click.mp3")

        if self.back_button.collide_point(*touch.pos):
            if click_sound:
                click_sound.play()

            self.app.change_screen(MainMenu(self.app))

    def lagu_kebangsaan(self, instance):
        print("Mulai Game Lagu Kebangsaan")

    def lagu_daerah(self, instance):
        print("Mulai Game Lagu Daerah")


class MainMenu(FloatLayout):
    def __init__(self, app, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.app = app

        self.top_bar = Image(
            source="public/img/TOP_BAR.png",
            size_hint=(1, 0.15),
            pos_hint={"center_x": 0.5, "top": 1},
            allow_stretch=True,
            keep_ratio=False,
        )
        self.add_widget(self.top_bar)

        self.middle_image = Image(
            source="public/img/burung.png",
            pos_hint={
                "center_x": 0.5,
                "top": 1.0,
            },
            size_hint=(0.7, 0.7),
        )
        self.add_widget(self.middle_image)

        self.bottom_bar = Image(
            source="public/img/BOTTOM_BAR.png",
            size_hint=(1, 0.15),
            pos_hint={"center_x": 0.5, "y": 0},
            allow_stretch=True,
            keep_ratio=False,
        )
        self.add_widget(self.bottom_bar)

        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        click_sound = SoundLoader.load("public/sound/click.mp3")

        self.start_button = OvalButton(
            click_sound=click_sound,
            text="Mulai Game",
            font_size="24px",
            font_name="public/font/satoshi.ttf",
            size_hint=(0.5, 0.10),
            background_color=(57 / 255, 171 / 255, 231 / 255, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.32},
        )
        self.start_button.bind(on_press=self.start_game)
        self.add_widget(self.start_button)

        self.exit_button = OvalButton(
            click_sound=click_sound,
            text="Keluar Game",
            font_size="24px",
            font_name="public/font/satoshi.ttf",
            size_hint=(0.5, 0.10),
            background_color=(1, 0, 0, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.2},
        )
        self.exit_button.bind(on_press=self.exit_game)
        self.add_widget(self.exit_button)

        self.update_mute_button()

    def update_mute_button(self):
        mute_image = ""

        if self.app.background_sound.state == "play":
            mute_image = "public/img/unmute.png"
        else:
            mute_image = "public/img/mute.png"

        self.mute_image = Image(
            source=mute_image,
            size_hint=(None, None),
            size=(30, 30),
            pos_hint={"x": 0.05, "top": 0.95},
        )
        self.mute_image.bind(on_touch_down=self.toggle_sound)
        self.add_widget(self.mute_image)

    def toggle_sound(self, instance, touch):
        if self.mute_image.collide_point(*touch.pos):
            if self.app.background_sound.state == "play":
                self.app.background_sound.stop()
                self.mute_image.source = "public/img/mute.png"
            else:
                self.app.background_sound.play()
                self.mute_image.source = "public/img/unmute.png"

            self.mute_image.reload()

            return True
        return False

    def start_game(self, instance):
        self.app.change_screen(ChooseGame(self.app))

    def exit_game(self, instance):
        App.get_running_app().stop()

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)

        self.title = "Nada Petualang Cilik"

        self.background_sound = SoundLoader.load("public/sound/bg1.mp3")
        if self.background_sound:
            self.background_sound.loop = True
            self.background_sound.volume = 0.5
            self.background_sound.play()

    def build(self):
        return MainMenu(self)

    def change_screen(self, new_screen):
        self.root.clear_widgets()
        self.root.add_widget(new_screen)


if __name__ == "__main__":
    try:
        MyApp().run()
    except KeyboardInterrupt:
        sys.exit(0)
