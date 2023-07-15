import random as ran
from tkinter import *

root=Tk()
root.geometry("750x750")
root.title("Password Generator")
l1=Label(root,text='',font=("times",20))

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
b1.pack()

root.mainloop()
