from turtle import Turtle
import time


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.sc = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 280)
        self.score_cr()

    def score_cr(self):
        self.clear()
        self.write(f"Score: {self.sc} High Score: {self.high_score}", False, align="center",
                   font=('Courier', 15, 'normal'))

    def reset(self):
        if self.sc > self.high_score:
            self.high_score = self.sc
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.sc = 0
        self.score_cr()
    #function to play one time
    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER !! YOUR SCORE {self.sc}", False, align="center", font=('Courier', 30, 'bold'))
