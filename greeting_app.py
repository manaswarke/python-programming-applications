from tkinter import *
from datetime import *

root = Tk()
root.title("Geometry App by Manas Warke")
root.geometry("600x500+300+20")
root.resizable(False, False)

f = ("Arial", 30, "bold")

def show():
    name = ent_name.get()
    if name == "":
        msg = "name should not be empty"
        lab_msg.configure(text=msg, fg="red")
        return
        
    if not name.replace(" ", "").isalpha():
        msg = "name should contain only alphabets"
        lab_msg.configure(text=msg, fg="red")
        return

    dt = datetime.now()
    hr = dt.hour
    if hr < 12:
        msg = "Good morning " + str(name)
    elif hr < 16:
        msg = "Good afternoon " + str(name)
    else:
        msg = "Good evening " + str(name)
        
   
    lab_msg.configure(text=msg, fg="blue")

lab_header = Label(root, text="Greeting App", font=f)
lab_header.pack(pady=20)

lab_name = Label(root, text="Enter Name", font=f)
lab_name.pack(pady=20)

ent_name = Entry(root, font=f)
ent_name.pack(pady=20)

btn_submit = Button(root, text="Submit", font=f, command=show)
btn_submit.pack(pady=10)

lab_msg = Label(root, text="", font=f)
lab_msg.pack(pady=20)

root.mainloop()