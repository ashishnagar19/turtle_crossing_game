from turtle import Turtle, Screen
from brick import Brick
from score import Score
import time
from gameover import GameOver
screen = Screen()
screen.setup(width=600, height=600)
screen.title("TURTLE CROSSING GAME")
screen.tracer(0)
brick = Brick()
score = Score()
gameover = GameOver()

turtle = Turtle()
turtle.shape("turtle")
turtle.penup()
turtle.goto(0, -280)
turtle.setheading(90)

def move_turtle():
    new_y = turtle.ycor()+10
    turtle.goto(0, new_y)

screen.listen()
screen.onkey(move_turtle, "Up")
move_turtle()




game = True
while game:
    time.sleep(0.1)
    screen.update()
    brick.create_brick()
    brick.move_brick()

    for car_2 in brick.car:
        if car_2.distance(turtle) < 20:
            game = False
            gameover.gameover()

    if turtle.ycor() > 280:
        turtle.goto(0, -280)
        brick.level_up()
        score.increase_level()






screen.exitonclick()