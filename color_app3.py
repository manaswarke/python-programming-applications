#color_app3 --> remove the button
#and after every 10secs color should change automatically

from tkinter import *
from random import *

root = Tk()
root.title("Color App v3")
root.geometry("600x600+300+30")
f = ("Arial", 50, "bold")

def c():
     colors = ["red", "green", "blue", "orange", "yellow", "gray", "violet", "pink"]
     r = choice(colors)
     root.configure(bg=r)
     root.after(5000,c)

c()

root.mainloop()

