from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_axis, y_axis):
        super().__init__()

        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x_axis, y=y_axis)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)    
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)     
