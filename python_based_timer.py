from random import randrange
from tkinter import Button, Label, Tk, StringVar, OptionMenu, Widget, font, Entry
import time
from tkinter import messagebox
from tkinter.constants import CURRENT, LEFT
import winsound


app_window = Tk() 
app_window.title("Digital Clock in Python") 
app_window.geometry("400x190")


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
question_menu.place(x=250,y=5)

background, foreground = colors[0]
text_font= ("Boulder", 68, 'bold')
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.place(x=0,y=40)

alarm = Label(app_window,text='Time (Hr:Min:Sec)',font = ('Boulder',10))
alarm.place(x=0,y=7)

entry = Entry(app_window,font=('cosmic sans',10),width=10)
entry.place(x=120,y=7)

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   background, foreground = colors[options_list.index(selection.get())]
   if time_live == entry.get():
     winsound.PlaySound("ringtone.wav",winsound.SND_LOOP + winsound.SND_ASYNC)
     msg = messagebox.showinfo('Wake Up!',"Wake up!")
     if msg:
        winsound.PlaySound(None, winsound.SND_FILENAME)
   label.config(text=time_live, bg=background, fg=foreground,justify=LEFT)
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
