from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.image import Image

from pages.level.layout import LayoutFinish, LayoutQuest

questions_data = [
    {
        "bg_sound": "assets/music/daerah/question/ampar_ampar_pisang.mp3",
        "lirik": [
            "Pisangku belum masak",
            "Masak sedikit, dihurung bari-bari",
            "Masak sedikit, dihurung bari-bari",
            "Mangga lepak mangga lepok",
            "Patah kayu bengkok",
            "Bengkok dimakan api",
            "Apinya canculupan"
        ],
        "jawaban": "a",
        "button_title": "assets/quest/level_2/daerah/q1/title.png",
        "btn_a_src": "assets/quest/level_2/daerah/q1/a.png",
        "btn_b_src": "assets/quest/level_2/daerah/q1/b.png",
        "btn_c_src": "assets/quest/level_2/daerah/q1/c.png",
    },  
    {
        "bg_sound": "assets/music/daerah/question/yamko_rambe_yamko.mp3",
        "lirik": [
            "Hee yamko rambe yamko aronawa kombe",
            "Hee yamko rambe yamko aronawa kombe",
            "Hongke hongke hongke riro",
            "Hongke jombe jombe riro",
            "Hongke hongke hongke riro",
            "Hongke jombe jombe riro"
        ],
        "jawaban": "b",
        "button_title": "assets/quest/level_2/daerah/q2/title.png",
        "btn_a_src": "assets/quest/level_2/daerah/q2/a.png",
        "btn_b_src": "assets/quest/level_2/daerah/q2/b.png",
        "btn_c_src": "assets/quest/level_2/daerah/q2/c.png",
    }, 
    {
        "bg_sound": "assets/music/daerah/question/rasa_sayange.mp3",
        "lirik": [
            "Rasa sayange.. rasa sayang sayange..",
            "Lihat nona dari jauh rasa sayang sayange",
            "Rasa sayange.. rasa sayang sayange..",
            "Lihat nona dari jauh rasa sayang sayange",
        ],
        "jawaban": "a",
        "button_title": "assets/quest/level_2/daerah/q3/title.png",
        "btn_a_src": "assets/quest/level_2/daerah/q3/a.png",
        "btn_b_src": "assets/quest/level_2/daerah/q3/b.png",  
        "btn_c_src": "assets/quest/level_2/daerah/q3/c.png",     
    }
]

class Daerah_Level_2(Screen):
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
        
        finish_template = LayoutFinish(app=self.app, point_quest=self.question_points, destination="lagu_daerah")
        self.add_widget(finish_template)

        self.current_question_index = 0
        self.points = 0
        self.question_points = {}
