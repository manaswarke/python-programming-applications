from tkinter import *

root = Tk()
root.title("Even Odd App by Manas Warke")
root.geometry("900x500+300+30")
f = ("Arial", 40, "bold")

lab_header = Label(root, text="Even Odd App", font=f)
lab_header.pack(pady=10)

lab_num = Label(root, text="Enter integer", font=f)
ent_num = Entry(root, font=f)
lab_num.pack(pady=20)
ent_num.pack(pady=10)

def check():
    try:
        num = int(ent_num.get())
        if num % 2 == 0:
            msg = str(num) + " is even"
        else:
            msg = str(num) + " is odd"
        lab_msg.configure(text=msg)
    except ValueError:
        msg = "please enter integers only"
        lab_msg.configure(text=msg)

btn_find = Button(root, text="Find Even/Odd", font=f, command=check)
lab_msg = Label(root, font=f)

btn_find.pack(pady=10)
lab_msg.pack(pady=10)  

root.mainloop()