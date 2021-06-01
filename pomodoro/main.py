from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
counter = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global counter
    global reps
    canvas.after_cancel(counter)
    canvas.itemconfig(timer,text='00:00')
    top_label.config(text='Timer', fg=GREEN,font=(FONT_NAME,30,'normal'),bg=YELLOW)
    check_mark.config(text='',fg=GREEN,highlightthickness=0,bg=YELLOW)
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        top_label.config(text='Break', fg=RED,font=(FONT_NAME,30,'normal'),bg=YELLOW)
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        top_label.config(text='Break', fg=PINK,font=(FONT_NAME,30,'normal'),bg=YELLOW)
        count_down(SHORT_BREAK_MIN*60)
    else:
        top_label.config(text='Work', fg=GREEN,font=(FONT_NAME,30,'normal'),bg=YELLOW)
        count_down(WORK_MIN*60)    

    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global counter
    min_count = math.floor(count/60)
    sec_count = count%60
    if sec_count < 10:
        sec_count = f'0{sec_count}'
    canvas.itemconfig(timer,text=f'{min_count}:{sec_count}')
    if count > 0:
        counter = window.after(1000,count_down, count-1)
    else:
        start_timer()
        mark = ''
        for i in range(math.floor(reps/2)):
            mark += '✅'
        check_mark.config(text=mark)    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

top_label = Label(text='Timer', fg=GREEN,font=(FONT_NAME,30,'normal'),bg=YELLOW)
top_label.grid(column=1,row=0)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato)
timer = canvas.create_text(102, 120, text='00:00', fill='white', font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


start_button = Button(text='Start',bg="#fff",border=0,highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset',bg="#fff",border=0,highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark = Label(text='',fg=GREEN,highlightthickness=0,bg=YELLOW)
check_mark.grid(column=1,row=3)

window.mainloop()
