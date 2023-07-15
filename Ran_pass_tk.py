import random as ran
from tkinter import *

root=Tk()   #creating root
root.geometry("750x750")
root.title("Password Generator")

l1=Label(root,text='',font=("times",20))  #Creating label

def roll():
    small="abcdefghijklmnopqrstuvwxyz"
    large="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="0123456789"
    special_char="!@#$%^&*"
    password=small+large+numbers+special_char
    size=int(input("What is your size of Password : "))
    l1.config(text=f'Your Password is :{"".join(ran.sample(password,size))}')
    l1.pack()

b1=Button(root,text=" Click to Generate a Confidential Password : ",bg='skyblue',fg='red',command=roll)
#pack() is mandatory to fix that widget into the GUI
b1.pack()
#ending of root
root.mainloop()
