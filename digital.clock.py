from tkinter import *
from datetime import *

root = Tk()
root.title("Digital Clock by Manas Warke")
root.geometry("1000x300+300+100")
root.resizable(False,False)
root.configure(bg="lightblue")

f = ("Arial", 120, "bold")

lab_time = Label(root, text="", font=f, bg="lightblue")
lab_time.pack(pady=50)

def show():
    dt = datetime.now()
    hr =dt.hour
    if hr < 10:
       hr = "0" + str(hr)
    mi  =dt.minute
    if mi < 10:
        mi = "0" + str(mi)
    se = dt.second
    if se < 10:
       se = "0" + str(se)

    msg = str(hr) + " : " + str(mi) + " : " + str(se)
    lab_time.configure(text=msg)
    root.after(1000,show)
show()

root.mainloop()