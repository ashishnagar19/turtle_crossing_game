import random
from turtle import Turtle
COLORS = ["orange", "red", "green", "blue", "black"]
STARTING_DISTANCE = 5
MOVE_INCREMENT = 5

class Brick():
    def __init__(self):
        self.car = []
        self.create_brick()
        self.car_speed = STARTING_DISTANCE



    def create_brick(self):
            random_chance = random.randint(1, 6)
            if random_chance==1:
                segment = Turtle("square")
                segment.color(random.choice(COLORS))
                segment.penup()
                segment.shapesize(stretch_len=2, stretch_wid=1)
                random_y = random.randint(-250, 250)
                segment.goto(280, random_y)
                self.car.append(segment)

    def move_brick(self):
        for car_ in self.car:
            car_.backward(self.car_speed)

    def level_up(self):
            self.car_speed+=MOVE_INCREMENT











