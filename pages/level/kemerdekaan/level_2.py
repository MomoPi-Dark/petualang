from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.image import Image

from pages.level.layout import LayoutFinish, LayoutQuest

questions_data = [
    {
        "bg_sound": "assets/music/kemerdekaan/question/dari_sabang_sampai_merauke.mp3",
        "lirik": [
            "Sambung-menyambung menjadi satu",
            "Itulah Indonesia",
            "Indonesia tanah airku",
            "Aku berjanji padamu",
        ],
        "jawaban": "b",
        "button_title": "assets/quest/level_2/kemerdekaan/q1/title.png",
        "btn_a_src": "assets/quest/level_2/kemerdekaan/q1/a.png",
        "btn_b_src": "assets/quest/level_2/kemerdekaan/q1/b.png",
        "btn_c_src": "assets/quest/level_2/kemerdekaan/q1/c.png",
    },  
    {
        "bg_sound": "assets/music/kemerdekaan/question/halo_halo_bandung.mp3",
        "lirik": [
            "Sudah lama beta",
            "Tidak Berjumpa dengan kau",
            "Sekarang sudah menjadi lautan api",
            "Mari Bung rebut kembali",
        ],
        "jawaban": "a",
        "button_title": "assets/quest/level_2/kemerdekaan/q2/title.png", 
        "btn_a_src": "assets/quest/level_2/kemerdekaan/q2/a.png",
        "btn_b_src": "assets/quest/level_2/kemerdekaan/q2/b.png",
        "btn_c_src": "assets/quest/level_2/kemerdekaan/q2/c.png",
    },
    {
        "bg_sound": "assets/music/kemerdekaan/question/satu_nusa_satu_bangsa.mp3",
        "lirik": [
            "Tanah Air",
            "Pasti Jaya Untuk Slama-lamanya"
        ],
        "jawaban": "c",
        "button_title": "assets/quest/level_2/kemerdekaan/q3/title.png",
        "btn_a_src": "assets/quest/level_2/kemerdekaan/q3/a.png",
        "btn_b_src": "assets/quest/level_2/kemerdekaan/q3/b.png",
        "btn_c_src": "assets/quest/level_2/kemerdekaan/q3/c.png",
    }
]

class Kemerdekaan_Level_2(Screen):
    def __init__(self, app, **kw):
        super().__init__(**kw)
        self.app = app
        
        self.bg_image_path = "assets/img/bg.png"
        
        self.current_question_index = 0
        self.points = 0
        self.question_points = {}

        self.bg = Image(source=self.bg_image_path,
                        allow_stretch=True,
                        keep_ratio=True)
        self.add_widget(self.bg)
        
    def _is_quiz_finished(self):
        return self.current_question_index >= len(questions_data)

    def on_enter(self, *args):
        super().on_enter(*args)
        self.load_question()

    def on_leave(self, *args):
        super().on_leave(*args)
        self.reset_screen()

    def reset_screen(self):
        """Clear the screen and reload the background."""
        self.clear_widgets()
        self.add_widget(Image(source=self.bg_image_path))

    def load_question(self):
        """Load the current question."""
        if self._is_quiz_finished():
            self.finish_quiz()
        else:
            question_data = questions_data[self.current_question_index]

            self.question_template = LayoutQuest(
                app=self.app,
                bg=self.bg_image_path,
                bg_sound=question_data["bg_sound"],
                descriptions=question_data["lirik"],
                result=question_data["jawaban"],
                button_title=question_data["button_title"],
                btn_a_src=question_data["btn_a_src"],
                btn_b_src=question_data["btn_b_src"],
                btn_c_src=question_data["btn_c_src"],
            )
            self.question_template.call_screen()
            self.question_template.bind(on_value_submit=self.on_question_answered)
            self.add_widget(self.question_template)

    def _set_question_point(self, point):
        """Set the points for the current question."""
        self.points += point
        self.question_points[f"question_{self.current_question_index}"] = point

    def on_question_answered(self, instance, is_correct, value):
        """Handle the question answer."""
        if is_correct:
            self._set_question_point(100)
        else:
            self._set_question_point(0)

        Clock.schedule_once(self.load_next_question, 3)

    def load_next_question(self, dt):
        """Load the next question after a short delay."""
        self.clear_widgets()
        if not self._is_quiz_finished():
            self.current_question_index += 1
            self.load_question()
        else:
            self.finish_quiz()

    def finish_quiz(self):
        """Display the finish screen with the final points."""
        self.reset_screen()
        
        finish_template = LayoutFinish(app=self.app, point_quest=self.question_points, destination="lagu_kemerdekaan")
        self.add_widget(finish_template)

        self.current_question_index = 0
        self.points = 0
        self.question_points = {}
