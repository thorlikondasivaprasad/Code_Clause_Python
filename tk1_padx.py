from tkinter import *

win= Tk()
win.geometry("700x700")

b1= Button(win, text= "Button1", font=('times bold', 15),bg='yellow')
b1.pack(padx=10,pady=50)

b2= Button(win, text= "Button2", font=('calibri bold', 15),bg='orange')
b2.pack(padx=50,pady=50)

b3= Button(win, text= "Button3", font= ('sans sarif bold', 15),bg='pink')
b3.pack(padx=50, pady=50)

win.mainloop()
