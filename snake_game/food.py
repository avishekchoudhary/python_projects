from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super(). __init__()

        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color('yellow')
        self.speed('fastest')
        self.food_refresh()
    

    def food_refresh(self):
        x_axis = random.randint(-280, 280)
        y_axis = random.randint(-280, 280)
        self.goto(x=x_axis,y=y_axis)
