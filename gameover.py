from turtle import Turtle


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def gameover(self):
        self.write(f"GAME OVER!", align="center", font=("Courier", 20, "normal"))

