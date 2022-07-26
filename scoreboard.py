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
        self.write(f"Score: {self.score}", align="center", font=("Times New Roman", 15, "normal"))

    def increase_score(self, points_scored=1):
        self.score += points_scored
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Comic Sans MS", 50, "bold"))
