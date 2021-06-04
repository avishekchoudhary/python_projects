from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')    
df = data.to_dict(orient='records')

current_wrd = {}


def wrd_remove():
    global current_wrd
    df.remove(current_wrd)
    change_word()
    new_data = pd.DataFrame(df) 
    new_data.to_csv('data/words_to_learn.csv', index=False)


def  change_word():
    global current_wrd,flip_timer
    window.after_cancel(flip_timer)
    current_wrd = random.choice(df)
    canvas.itemconfig(lan, text='French',fill='black')
    canvas.itemconfig(word, text=f'{current_wrd["French"]}',fill='black')
    canvas.itemconfig(card_image, image=front_image)
    flip_timer = window.after(3000, func=card_flip)

def card_flip():
    canvas.itemconfig(lan, text='English',fill='white')
    canvas.itemconfig(word, text=f'{current_wrd["English"]}',fill='white')
    canvas.itemconfig(card_image, image=back_image)



window = Tk()
window.title('Language Flashcard')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=card_flip)



canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
card_image = canvas.create_image(400,263,image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

lan = canvas.create_text(400, 150, text='', font=('Arial',40,'italic'))
word = canvas.create_text(400, 263, text='', font=('Arial',60,'italic'))

bt_right_image = PhotoImage(file='images/right.png') 
bt_wrong_image = PhotoImage(file='images/wrong.png')

right_bt = Button(image=bt_right_image,highlightthickness=0,border=0,command=wrd_remove)
right_bt.grid(column=0,row=1)

wrong_bt = Button(image=bt_wrong_image,highlightthickness=0,border=0, command=change_word)
wrong_bt.grid(column=1,row=1)


change_word()


















window.mainloop()