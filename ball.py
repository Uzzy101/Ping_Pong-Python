from turtle import Turtle
import random

COLORS = ["blue", "red", "green", "purple", "cyan", "pink", "orange"]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(random.choice(COLORS))
        self.penup()
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.move_factor = 10
        self.move_factor2 = 10

    def move(self):
        self.x_coordinate += self.move_factor2
        self.y_coordinate += self.move_factor
        self.goto(self.x_coordinate, self.y_coordinate)

        if self.ycor() >= 280:
            self.move_factor = -10

        if self.ycor() <= -280:
            self.move_factor = 10

    def collision(self):
        self.move_factor2 = -self.move_factor2
        self.color(random.choice(COLORS))

    def restart(self):
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.move_factor2 = -self.move_factor2
        self.move_factor = self.move_factor
