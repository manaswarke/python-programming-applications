from tkinter import*
from random import *

root = Tk()
root.title("Color App v2")
root.geometry("600x600+300+30")
f = ("Arial", 50, "bold")

def c():
    colors = ["red", "green", "blue", "orange", "yellow", "grey"]
    r = choice(colors)
    root.configure(bg=r)

btn = Button(root, text="Color Me", font=f, command=c)
btn.pack(pady=20)

root.mainloop()