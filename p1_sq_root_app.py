from tkinter import *

root = Tk()
root.title("Square root App by Manas")
root.geometry("1100x500+300+50")
f = ("Times New Roman", 40, "bold")

lab_header = Label(root, text="Square Root finder", font=f)
lab_header.place(x=300,y=20)

lab_number = Label(root, text="Enter Number", font=f)
ent_number = Entry(root, font=f)
lab_number.place(x=50, y=120)
ent_number.place(x=450, y=120)

def find():
        try:
              num = float(ent_number.get())
              if num >=0:
                      sqrt = num ** (1/2)
                      msg = "Square Root of " + str(num) + "is " + str(round(sqrt,2))
                      lab_msg.configure(text=msg, fg="blue")
              else:
                      msg = "please enter +ve numbers only"
                      lab_msg.configure(text=msg,fg="red")
        except ValueError:
               msg = "please enter numbers only"
               lab_msg.configure(text=msg,fg="red")

btn_find = Button(root, text="Find Square Root", font=f,command=find)
lab_msg = Label(root, text="", font=f)
btn_find.place(x=450,y=220)
lab_msg.place(x=50,y=350)

root.mainloop()
