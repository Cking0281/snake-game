from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.pencolor("white")
        self.pendown()

    def display_score(self):
        self.write(arg=f"Score: {self.score}", align="center", font=("Times New Roman", 15, "normal"))

    def increase_score(self, points_scored=1):
        self.score += points_scored
        self.clear()
        self.display_score()
