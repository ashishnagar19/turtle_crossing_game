from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.l_score = 1
        self.goto(-230, 250)
        self.hideturtle()
        self.update_score()

    def increase_level(self):
        self.clear()
        self.l_score+=1
        self.update_score()

    def update_score(self):
        self.write(f"LEVEL:{self.l_score}", align="center", font=("Courier", 20, "normal"))

