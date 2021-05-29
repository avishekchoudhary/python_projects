from turtle import Screen, screensize
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

SLEEP_TIME = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.title('PONG')
screen.bgcolor('black')
screen.tracer(0)

paddle_l = Paddle(x_axis=350, y_axis=0)
paddle_r = Paddle(x_axis=-350, y_axis=0)

ball = Ball()

score = Score()


is_game_on = True





screen.listen()
screen.onkey(paddle_l.up, 'Up')
screen.onkey(paddle_l.down, 'Down')
screen.onkey(paddle_r.up, 'w')
screen.onkey(paddle_r.down, 's')




while is_game_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    ball.ball_dance()

    if ball.ycor() > 277 or ball.ycor() <- 277:
        ball.bounce_vertical() 
        SLEEP_TIME *= 0.9 

    if ball.distance(paddle_l) < 50  or ball.distance(paddle_r) < 50 :
        ball.bounce_horizontal()
        SLEEP_TIME *= 0.9

    if ball.xcor() < -380:
        ball.reset()
        score.update_r()
        SLEEP_TIME = 0.1

    if ball.xcor() > 380:
        ball.reset() 
        score.update_l()
        SLEEP_TIME = 0.1

    




screen.exitonclick()