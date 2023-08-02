from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Le pong game.")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
l_paddle.x_coordinate = -350
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")

game_is_on = True
time_factor = 0.1

while game_is_on:
    time.sleep(time_factor)
    screen.update()
    ball.move()

    if r_paddle.distance(ball) < 40 and ball.xcor() > 320 or l_paddle.distance(ball) < 40 and ball.xcor() < -320:
        ball.collision()
        time_factor *= 0.9

    if ball.xcor() > 400:
        ball.restart()
        score.goal_l()
        time_factor = 0.1

    if ball.xcor() < - 400:
        ball.restart()
        score.goal_r()
        time_factor = 0.1
screen.exitonclick()
