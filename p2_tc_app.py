from tkinter import *

root = Tk()
root.title("Temperature Converter by Manas Warke")
root.geometry("900x550+300+50")
f = ("Times New Roman", 30, "bold")

lab_header = Label(root, text = "Temperature Converter App", font=f)
lab_header.place(x=300, y=20)

lab_temperature = Label(root, text="Enter temperature", font=f)
ent_temperature = Entry(root, font=f)
lab_temperature.place(x=50, y=120)
ent_temperature.place(x=450,y=120)

def convert():
         try:
                   temp = float(ent_temperature.get())
                   if c.get() == 1:
                           ans = (temp * 1.8) + 32
                           msg = str(temp) + " in cel = " + str(round(ans,2)) + "in fah"
                   else:
                           ans = (temp-32)/1.8
                           msg = str(temp) + " in fah =" + str(round(ans,2)) + " in cel"
                   lab_msg.configure(text=msg,fg="blue")
 
         except ValueError:
                   msg = "please enter temperatures in numbers only"
                   lab_msg.configure(text=msg, fg="red")


c = IntVar()
c.set(1)
lab_select = Label(root, text="Select One", font=f)
lab_select.place(x=50,y=220)
rb_c2f = Radiobutton(root, text="c2f", font=f, variable=c, value=1)
rb_f2c = Radiobutton(root, text="f2c", font=f, variable=c, value=2)
rb_c2f.place(x=450, y=220)
rb_f2c.place(x=450, y=270)

btn_convert = Button(root, text="Convert",font=f,command=convert)
lab_msg = Label(root,text="", font=f)
btn_convert.place(x=450,y=350)
lab_msg.place(x=50, y=450)

root.mainloop()