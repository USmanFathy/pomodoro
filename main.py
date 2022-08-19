import math

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
time_parts = 0
Timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    screen.after_cancel(Timer)
    title.config(text="Timer", fg= GREEN)
    mark.config( fg= GREEN , bg= YELLOW)
    canvas.itemconfig(timer , text ="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count ():
    global time_parts

    time_parts +=1

    work_sec= WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN *60

    
    if time_parts % 8 == 0 :
        count_down(long_break_sec)
        title.config(text="BREAK", fg= RED)
    elif time_parts %2 == 0 :
        count_down(short_break_sec)
        title.config(text="BREAK", fg= PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg= GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/ 60)
    count_sec = count % 60
    if count_sec < 10 :
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer , text =f"{count_min}:{count_sec}")
    if count > 0 :
        global Timer
        Timer = screen.after(1000 , count_down , count-1)
    else:
        start_count()
        if time_parts%2 == 0 :
            mark.config(text='✔' )
# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()

screen.title('pomodoro')
screen.config(padx=100 , pady=50 , bg= YELLOW)




title = Label(text='Timer' ,fg=GREEN , bg=YELLOW , font=(FONT_NAME , 50))
title.grid(column=1 , row=0)


canvas = Canvas(width=200 , height=224 , highlightthickness=0 , bg= YELLOW)
img = PhotoImage(file='tomato.png')
canvas.create_image(100 , 112 , image= img)
timer =canvas.create_text(100, 130 , text="00:00" , fill= "white" , font=(FONT_NAME , 35 , "bold"))
canvas.grid(column=1 , row=1)


start = Button(text='Start' , highlightthickness=0 , command=start_count)
start.grid(column=0 , row=2)
reset = Button(text='Reset' , highlightthickness=0 , command=reset_timer)
reset.grid(column=2 , row=2)


mark = Label( fg= GREEN , bg= YELLOW)
mark.grid(column=1 , row=3)


screen.mainloop()