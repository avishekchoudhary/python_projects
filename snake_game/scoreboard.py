from turtle import  Turtle




class Score(Turtle):

    def __init__(self):
        super(). __init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.color('white')
        self.score = 0
        with open('data.txt') as file:
            data = file.read()
            self.highscore = int(data)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f'Score: {self.score}    HighScore:{self.highscore}', move=False, align= 'center',font=("Courier", 24, "normal")) 

    def score_increase(self):
        self.score +=1
        self.score_update()
    

    def score_reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', 'w') as data:
                data.write(f'{self.highscore}')
        self.score = 0        
        self.score_update()
    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", move=False, align= 'center',font=("Courier", 24, "normal"))    