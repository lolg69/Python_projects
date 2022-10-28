from cgitb import text
from tkinter import *

root = Tk()

def click_me():
    name = e.get()
    myLabel = Label(root, text="Help I was ra... Clicked!" + name)
    myLabel.pack()

e = Entry(root, text="Nahtrto")
e.pack()
e.insert(0, "Something smart")

my_button = Button(text="Click me!",command=click_me)
my_button.pack()

root.mainloop()