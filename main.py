from tkinter import *
import  math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_marl = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=YELLOW)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count/60)
    seconds = (count % 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += check_marl
        check_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)

#timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=PINK)
timer_label.grid(column=1,row=0)
timer_label.config(padx=100,pady=10)

#check label
check_label = Label(fg=GREEN, bg=PINK, font=(FONT_NAME, 30, "bold"))
check_label.grid(column=1,row=4)
check_label.config(pady=20)

#start button
start = Button(text="Start",command=start_timer)
start.grid(column=0,row=3)

#Reset button
reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=3)


canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)








window.mainloop()