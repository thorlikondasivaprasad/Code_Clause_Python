import random as ran

small_alphabets="abcdefghijklmnopqrstuvwxyz"

large_alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers="0123456789"

special_characters="!@#$%^&*"

password=small+large+numbers+special_char

size=int(input("What is your size of Password : "))

print("Your Confidential Password is :"," ".join(ran.sample(password,size)))
