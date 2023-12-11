from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as h_score:
            self.high_score = int(h_score.read())
        self.score = 0
        self.color("white")
        self.show_score()

    def show_score(self):
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial",22,"normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.show_score()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as h_score:
                self.high_score = self.score
                h_score.write(str(self.high_score))
        self.score = 0
        self.show_score()

