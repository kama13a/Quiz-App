from pydoc import text
from tkinter import *
from quiz_brain import QuizBrain
from utils import resource_path
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)

        #TODO: Score Label that changes every time when answer is correct
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Helvetica", 12, "bold"))
        self.score.grid(row=0, column=1, padx=20, pady=20)


        #TODO: Canvas that have a question from data.py
        self.canvas = Canvas(bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125,
                                                 text="hi",
                                                 font=("Arial", 20, "italic"),
                                                 width=280,
                                                 fill=THEME_COLOR
                                                )
        self.canvas.grid(row=1, column=0, padx=20,pady=20, columnspan=2)


        #TODO: Correct Button with image
        true_image = PhotoImage(file=resource_path("images/true.png"))
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.pressed_true)
        self.true_button.grid(row=2, column=0, pady=20, padx=20)


        #TODO: X button with image
        false_image = PhotoImage(file=resource_path("images/false.png"))
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.pressed_false)
        self.false_button.grid(row=2,column=1, pady=20, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz ")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def pressed_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def pressed_false(self):
        is_false = self.quiz.check_answer("False")
        self.give_feedback(is_false)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)