from random import randrange
from tkinter import Label, Tk, StringVar, OptionMenu
import time

app_window = Tk() 
app_window.title("Digital Clock in Python") 
app_window.resizable(1,1)

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

options_list = ["Dark", "Dark Inverse", "B&W", "B&W Inverse", "Blue", "Blue Inverse", "Apocalypse", "Apocalypse Inverse", "Struggle", "Struggle Inverse", "Juggler", "Juggler Inverse", "Pluto", "Pluto Inverse"]

selection = StringVar(app_window)
selection.set("Dark")
question_menu = OptionMenu(app_window, selection, *options_list)
question_menu.grid(row=0, column=1)

background, foreground = colors[0]
text_font= ("Boulder", 68, 'bold')
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=1, column=1)

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   background, foreground = colors[options_list.index(selection.get())]
   label.config(text=time_live, bg=background, fg=foreground)
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
