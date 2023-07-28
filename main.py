"""---------------------------------------- Dangerous Writing App (GUI Desktop) ----------------------------------------
The Most Dangerous Writing App is a web application for free writing that combats writer's block by deleting
all progress if the user stops typing for five seconds. It is targeted at creative writers who want to write
first drafts without worrying about editing or formatting.
Developer:	Manuel Ebert
Release: February 29, 2016
Platform:	Web Application
Type:	Text editor
License:	GNU General Public Licence
Website:	www.squibler.io/dangerous-writing-prompt-app

In this code, I make the desktop version of this app.
The user starts writing and if the user stops writing for more than 10 seconds or deletes more than 50 words,
the program stops.

In this version, the text written by the user before stopping the program is saved in a file for him.
"""

# ---------------------------------------- Add Required Library ----------------------------------------

from tkinter import Tk, PhotoImage, Canvas, Text, SE, END, messagebox
from datetime import datetime as dt

# ---------------------------------------- Add Parameters ----------------------------------------

BACKGROUND_COLOR = "#461959"
FONT_COLOR = "#AED8CC"
TEXT_COLOR = "#7A316F"
BUTTON_COLOR = "#CD6688"
FONT_NAME = "Arial"
event_time = []
events = []

# ---------------------------------------- Processor Function ----------------------------------------


def time_calculator(event):
    new_word_time = dt.now()
    event_time.append(new_word_time)


def deleted_calculator(event):
    events.append(event.keysym)
    last_events = events[-10:]
    if len(last_events) >= 10 and set(last_events) == {event.keysym}:
        messagebox.showerror('End', 'Error: You missed your Chance!')
        root.destroy()


def check_interval():
    now = dt.now()
    if event_time:
        time_delta = now - event_time[-1]
        time_delta = time_delta.total_seconds()
        if time_delta > 10:
            messagebox.showerror('End', 'Error: You missed your Chance!')
            root.destroy()
    root.after(1000, check_interval)

# ---------------------------------------- GUI Creation ----------------------------------------


root = Tk()
root.title("Dangerous Writing GUI App")
root.configure(width=600, height=400)
root.configure(bg='#461959')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img = PhotoImage(file="images/writing.png")
img_background = canvas.create_image(125, 175, image=img)
img_title = canvas.create_text(400, 25, text="Welcome to Dangerous Writing App", fill=FONT_COLOR,
                               font=(FONT_NAME, 20, "bold"))
img_description = canvas.create_text(500, 75, text="ok let's start!", fill=FONT_COLOR, font=(FONT_NAME, 20, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

text_box = Text(bg=TEXT_COLOR, fg=FONT_COLOR, width=67, height=24)
text_box.grid(row=0, column=1, sticky=SE, padx=10, pady=10)
text = text_box.get("1.0", END)

root.bind('<space>', lambda event: time_calculator(event))
root.bind('<BackSpace>', lambda event: deleted_calculator(event))

check_interval()
root.mainloop()
