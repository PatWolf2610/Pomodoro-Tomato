from cgitb import text
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
CHECKMARK = '✔'
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_count,text='00:00')
    timer_name.config(text='Timer')
    check_mark.config(text='')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if  reps % 2 != 0:
        count_down(25*60)
        timer_name.config(text='Working',foreground=GREEN)
    if reps % 2 == 0 and reps % 8 != 0:
        count_down(5*60)
        timer_name.config(text='Break',foreground=PINK)
    if reps % 8 == 0 :
        count_down(20*60)
        timer_name.config(text='Long Break',foreground=RED)
    if reps % 2 == 0:
        check_mark.config(text=(reps//2)*CHECKMARK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_count,text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_mark.config(text=(reps//2)*CHECKMARK)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=80,bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image =tomato_img)
timer_count = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)

#Label Timer
timer_name = Label(text='Timer',font=(FONT_NAME,40,'bold'),foreground=GREEN,background=YELLOW)
timer_name.grid(row=0,column=1)

#start button
start_button = Button(text='Start',width=8,highlightthickness=0,bd=1,command=start_timer)
start_button.grid(row=2,column=0)

#stop button
reset_button = Button(text='Reset',width=8,highlightthickness=0,bd=1,command=reset_timer)
reset_button.grid(row=2,column=2)

#check text
check_mark = Label(font=('Arial',20,'bold'),foreground=GREEN,background=YELLOW)
check_mark.grid(row=3,column=1)

window.mainloop()
