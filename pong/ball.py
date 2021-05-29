from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(). __init__()

        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_step = 10
        self.y_step = 10

    def ball_dance(self):
        new_x = self.xcor() +self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)   

    def bounce_vertical(self):
        self.y_step *= -1

    def bounce_horizontal(self):
        self.x_step *= -1    

    def reset(self):
        self.goto(0, 0)
        self.x_step *= -1
          