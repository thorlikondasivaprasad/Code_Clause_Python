from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()
root.title=("CLock")

# %A - full weekday's name -> ex: Wednesday
# %x - appr. date from system -> ex: 12/12/2012
# %H - 24 hours time format
# %I - 12 hours time format
# %M - minutes( 0...59)
# %S - Seconds( 0...59)

def time():
    string=strftime('%I:%M:%S %p \n %A \n %x')
    label.config(text=string)
    label.after(1000,time)
    
label=Label(root,font=('ariel',80),background = "black",foreground= "cyan")
label.pack(anchor='center')
time()

mainloop()
