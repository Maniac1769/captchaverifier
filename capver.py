from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
text = 'abcdefghijklmnopqrstuvwxyz0123456789'
root = Tk()
root.title("Captcha verification App")
root.geometry("400x400")
root.configure(bg='light blue')
captcha = StringVar()
input = StringVar()
cap_label = Label(root, text = 'CAPTCHA LENGTH', font = 'arial 10 bold').pack()
cap_len = IntVar()
length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = cap_len , width = 15).pack()
#####define function
pass_str = StringVar()
def Generator():
    captcha = ''
    for x in range (0,4):
        captcha = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(cap_len.get()- 4):
        captcha = captcha+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(captcha)
Button(root, text = "GENERATE CAPTCHA" , command = Generator ).pack(pady= 5)
########function to copy
def check():
    if pass_str.get() == input.get():
        messagebox.showinfo('Captcha Verification', 'Captcha verified Succesfully..')
    else:
        messagebox.showerror('Captcha Verification', 'Incorrect Captcha')
    input.set('')
    Generator()
Label(root, textvariable=pass_str, font="ariel 16 bold").pack(padx=5, pady=5)
Entry(root, textvariable=input, bg='white', font="ariel 12 bold").pack(padx=5, pady=5)
Button(root, text="Check", font="ariel 15 bold", bg='gold', command=check).pack(padx=5, pady=5)
Generator()
root.mainloop()
