from tkinter import *

root = Tk()

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear_arena():
    e.delete(0, END)

def add_arena():
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)
    global opr 
    opr = 1

def sub_arena():
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)
    global opr 
    opr = 2

def mul_arena():
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)
    global opr 
    opr = 3

def div_arena():
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)
    global opr 
    opr = 4
    

def equals():
    if opr == 1:
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num + int(second_number))
    elif opr == 2:
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num - int(second_number))
    elif opr == 3:
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num * int(second_number))
    elif opr == 4:
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num / int(second_number))

e = Entry(root, width=27,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)

b1 = Button(root, text="7",padx=20,pady=20,command=lambda:button_click(7))
b1.grid(row=1,column=0)

b2 = Button(root, text="8",padx=20,pady=20,command=lambda:button_click(8))
b2.grid(row=1,column=1)

b3 = Button(root, text="9",padx=20,pady=20,command=lambda:button_click(9))
b3.grid(row=1,column=2)

b4 = Button(root, text="4",padx=20,pady=20,command=lambda:button_click(4))
b4.grid(row=2,column=0)

b5 = Button(root, text="5",padx=20,pady=20,command=lambda:button_click(5))
b5.grid(row=2,column=1)

b6 = Button(root, text="6",padx=20,pady=20,command=lambda:button_click(6))
b6.grid(row=2,column=2)

b7 = Button(root, text="1",padx=20,pady=20,command=lambda:button_click(1))
b7.grid(row=3,column=0)

b8 = Button(root, text="2",padx=20,pady=20,command=lambda:button_click(2))
b8.grid(row=3,column=1)

b9 = Button(root, text="3",padx=20,pady=20,command=lambda:button_click(3))
b9.grid(row=3,column=2)

b0 = Button(root, text="0",padx=20,pady=20,command=lambda:button_click(0))
b0.grid(row=4,column=0)

sub = Button(root, text="-",padx=20,pady=20,command=sub_arena)
sub.grid(row=4,column=1)

add = Button(root, text="+",padx=20,pady=20,command=add_arena)
add.grid(row=4,column=2)

mul = Button(root, text="*",padx=20,pady=20,command=mul_arena)
mul.grid(row=5,column=1)

div = Button(root, text="/",padx=20,pady=20,command=div_arena)
div.grid(row=5,column=2)

equal = Button(root, text="=",padx=18,pady=20,command=equals)
equal.grid(row=5,column=0)

clear = Button(root, text="Clear",padx=70,pady=20,command=clear_arena)
clear.grid(row=6,column=0,columnspan=3)

root.mainloop()