from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_point = 0
        self.r_point = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_point, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_point, align="center", font=("Courier", 80, "normal"))

    def goal_l(self):
        self.l_point += 1
        self.update_score()

    def goal_r(self):
        self.r_point += 1
        self.update_score()
