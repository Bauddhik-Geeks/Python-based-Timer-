from tkinter import Label, Tk, PhotoImage
import time
app_window = Tk()
app_window.title("Digital Clock in Python")
app_window.geometry("500x300")
app_window.resizable(1, 1)

text_font = ("Boulder", 68, 'bold')
background = PhotoImage(file="img.png")
foreground = "red"

background_lable = Label(app_window, image=background)
background_lable.place(x=0, y=0)
label = Label(app_window, font=text_font,
              fg=foreground)
label.grid(row=0, column=1)
#label.pack(pady = 0)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)


digital_clock()
app_window.mainloop()
