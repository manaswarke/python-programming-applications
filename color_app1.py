from tkinter import *

root = Tk()
root.title("Color App v1")
root.geometry("600x600+300+30")
f = ("Arial", 30, "bold")

def r():
    root.configure(bg="red")
def g():
    root.configure(bg="green")
def b():
    root.configure(bg="blue")

btn_red = Button(root, text="Red", font=f, width=8, command=r)
btn_green = Button(root, text="Green", font=f, width=8, command=g)
btn_blue = Button(root, text="Blue", font=f, width=8, command=b)

btn_red.pack(pady=20)
btn_green.pack(pady=20)
btn_blue.pack(pady=20)

root.mainloop()