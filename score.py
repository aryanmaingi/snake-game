from turtle import Turtle
import time


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.sc = 0
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 280)
        self.score_cr()

    def score_cr(self):
        self.clear()
        self.write(f"Score: {self.sc}", False, align="center", font=('Courier', 15, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER !! YOUR SCORE {self.sc}", False, align="center", font=('Courier', 30, 'bold'))
