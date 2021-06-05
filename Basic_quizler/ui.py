from os import get_terminal_size
from tkinter import * 
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class quizInt:
    def __init__(self,quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title('Quiz_App')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text=f'Score:0',fg='#fff',bg=THEME_COLOR,highlightthickness=0)
        self.score_label.grid(column=1,row=0,pady=(5,10))


        self.canvas = Canvas(width=300,height=250)
        self.ques = self.canvas.create_text(150,125,width=280,text='',font=('Arial',20,'italic'))
        self.canvas.grid(column=0,row=1,columnspan=2)

        right_img = PhotoImage(file='images/true.png')
        wrong_img = PhotoImage(file='images/false.png')
        self.right_button = Button(image=right_img,border=0,highlightthickness=0, command=self.true_press)
        self.right_button.grid(column=0,row=2, pady=(10,10))

        self.wrong_button = Button(image=wrong_img,border=0,highlightthickness=0,command=self.false_press)
        self.wrong_button.grid(column=1,row=2,pady=(10,10))
    

        self.get_nxt_que()    


        self.window.mainloop()


    def get_nxt_que(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions() == True:
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques, text = q_text)    
        else:
            self.canvas.itemconfig(self.ques, text="Hurray, you have completed the quiz")   
            self.right_button.config(state='disabled') 
            self.wrong_button.config(state='disabled') 

    def true_press(self):
        is_right = self.quiz.check_answer('True')
        self.feedback(is_right)


    def false_press(self):
        is_right = self.quiz.check_answer('False')
        self.feedback(is_right)
        
    def feedback(self,answer):
        if answer == True:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')           
        self.window.after(1000, self.get_nxt_que)