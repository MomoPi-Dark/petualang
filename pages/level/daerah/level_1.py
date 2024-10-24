from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.image import Image

from pages.level.layout import LayoutFinish, LayoutQuest


questions_data = [
    {
        "descriptions": [
            "Lagu Ampar Ampar Pisang",
            "berasal dari daerah?",
        ],
        "jawaban": "a",
        "button_title": "assets/quest/level_1/daerah/q1/title.png",
        "btn_a_src": "assets/quest/level_1/daerah/q1/a.png",
        "btn_b_src": "assets/quest/level_1/daerah/q1/b.png",
        "btn_c_src": "assets/quest/level_1/daerah/q1/c.png",
    },
    {
        "descriptions": [
            "Lagu Cublak-cublak Suweng",
            "berasal dari daerah?",
        ],
        "jawaban": "a",
        "button_title": "assets/quest/level_1/daerah/q2/title.png",
        "btn_a_src": "assets/quest/level_1/daerah/q2/a.png",
        "btn_b_src": "assets/quest/level_1/daerah/q2/b.png",
        "btn_c_src": "assets/quest/level_1/daerah/q2/c.png",
    },
    {
        "descriptions": [
            "Lagu Sinanggar Tulo berasal dari daerah?",
        ],
        "jawaban": "b",
        "button_title": "assets/quest/level_1/daerah/q3/title.png",
        "btn_a_src": "assets/quest/level_1/daerah/q3/a.png",
        "btn_b_src": "assets/quest/level_1/daerah/q3/b.png",
        "btn_c_src": "assets/quest/level_1/daerah/q3/c.png",
    }
]

class Daerah_Level_1(Screen):
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
                descriptions=question_data["descriptions"],
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
        """Finish the quiz and show the result."""
        self.reset_screen()
        
        finish_template = LayoutFinish(app=self.app, point_quest=self.question_points, destination="lagu_daerah")
        self.add_widget(finish_template)
        
        self.current_question_index = 0
        self.points = 0
        self.question_points = {}