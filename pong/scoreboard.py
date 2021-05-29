from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super(). __init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.score_r = 0
        self.goto(100, 250)
        self.write(f'{self.score_r}', move=False, align= 'center',font=("Courier", 24, "normal"))
        self.score_l = 0
        self.goto(-100, 250)
        self.write(f'{self.score_l}', move=False, align= 'center',font=("Courier", 24, "normal"))
    

    def update_l(self):
        self.score_l += 1
        self.clear()
        self.write(f'{self.score_l}', move=False, align= 'center',font=("Courier", 24, "normal"))    

    def update_r(self):
        self.score_r += 1
        self.clear()
        self.write(f'{self.score_r}', move=False, align= 'center',font=("Courier", 24, "normal"))        