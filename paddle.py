from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, staring_positon):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.y_coordinate = 0
        self.x_coordinate = 350
        self.speed("fastest")
        self.penup()
        self.shapesize(5, 1)
        self.goto(staring_positon)

    def up(self):
        if self.ycor() <= 250:
            self.y_coordinate += 20
            self.goto(self.x_coordinate, self.y_coordinate)
        elif self.ycor() > 250:
            self.goto(self.x_coordinate, 250)

    def down(self):
        if self.ycor() >= -250:
            self.y_coordinate -= 20
            self.goto(self.x_coordinate, self.y_coordinate)
        elif self.ycor() < -250:
            self.goto(self.x_coordinate, -250)
