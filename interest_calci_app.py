from tkinter import *

root = Tk()
root.title("Interest Calci App by Manas")
root.geometry("900x650+300+50")
f = ("Times New Roman", 20, "bold")

lab_header = Label(root, text="Interest Calci App", font=f)
lab_header.place(x=300, y=20)
lab_principal = Label(root, text="Enter Principal Amount", font=f)
ent_principal = Entry(root, font=f)
lab_principal.place(x=50,y=120)
ent_principal.place(x=450, y=120)

lab_roi = Label(root, text="Enter Rate of Interest", font=f)
ent_roi = Entry(root, font=f)
lab_roi.place(x=50,y=180)
ent_roi.place(x=450, y=180)

lab_time = Label(root, text="Enter Time in years",font=f)
ent_time = Entry(root, font=f)
lab_time.place(x=50, y=240) 
ent_time.place(x=450, y=240)

def find():
        try:
                principal = float(ent_principal.get())
        except ValueError:
                msg = "principa; amt shud not be empty"
                lab_msg.configure(text=msg,fg="red")
                ent_principal.focus()
                return
        if principal < 1000:
                msg = "principal amt shud be min 1000"
                lab_msg.configure(text=msg,fg="red")
                ent_principal.focus() 
                return
        try:
                roi = float(ent_roi.get())
        except ValueError:
                msg = "roi shud not be empty"
                lab_msg.configure(text=msg,fg="red")
                ent_roi.focus()
                return

        if roi < 3:
                msg = "roi shud be min 3%"
                lab_msg.configure(text=msg, fg="red")
                ent_principal.focus()
                return
        try:
                time = float(ent_time.get())
        except ValueError:
                msg = "time shud not be empty"
                lab_msg.configure(text=msg,fg="red")
                ent_time.focus()
                return
        if time < 1:
                msg = "time shud be min 1 year"
                lab_msg.configure(text=msg, fg="red")
                ent_time.focus()
        if c.get():
                 si = (principal * roi * time)/100
                 msg = "Simple Interest = " + str(round(si,2))
        else:
                 ci = (principal * (1 + roi/100) ** time) - (principal)
                 msg = "Compound Interest = " + str(round(ci,2))
        lab_msg.configure(text=msg, fg="blue")

c = IntVar()
c.set(1)
lab_select = Label(root, text="Select One", font=f)
lab_select.place(x=50, y=320)
rb_si = Radiobutton(root,text="Simple Interest", font=f,variable=c, value=1)
rb_ci = Radiobutton(root,text="Compound Interest", font=f,variable=c, value=2)
rb_si.place(x=450,y=320)
rb_ci.place(x=450,y=370)

btn_find = Button(root, text="Find amount", font=f, command=find)
lab_msg = Label(root,text="", font=f)
btn_find.place(x=450, y=450)
lab_msg.place(x=50, y=550)

root.mainloop()