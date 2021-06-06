from turtle import Turtle, position, right

STARTING_COORDINATES = [(0,0), (-20,0), (-40,0)]
SNAKE_STEP = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position  in STARTING_COORDINATES:
            self.add_segment(position= position)
            
    def add_segment(self, position):
        snake_segment = Turtle(shape='square')
        snake_segment.color('white')
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(position= self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(SNAKE_STEP)

    def snake_reset(self):
        [seg.goto(1000,1000) for seg in self.segments]
        self.segments.clear()  
        self.create_snake()

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].seth(UP)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].seth(DOWN)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].seth(LEFT)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].seth(RIGHT)           


         