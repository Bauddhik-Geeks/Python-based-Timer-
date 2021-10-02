from random import randrange
from tkinter import Label, Tk, PhotoImage
import time

app_window = Tk()
app_window.title("Digital Clock in Python")
app_window.resizable(1, 1)

colors = [
    ("black", "red"),
    ("red", "black"),
    ("white", "black"),
    ("black", "white"),
    ("blue", "white"),
    ("white", "blue"),
    ("blue", "yellow"),
    ("yellow", "blue"),
    ("green", "pink"),
    ("pink", "green"),
    ("green", "yellow"),
    ("yellow", "green"),
    ("blue", "red"),
    ("red", "blue"),
]

background, foreground = colors[randrange(len(colors))]
background_image = PhotoImage(file="img.png")

text_font = ("Boulder", 68, 'bold')
border_width = 25

bg_label = Label(app_window, image=background_image)
bg_label.place(x=0, y=0)

label = Label(app_window, font=text_font, bg=background,
              fg=foreground, bd=border_width)
label.pack(pady=0)


def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)


digital_clock()
app_window.mainloop()
