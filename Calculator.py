"""A Graphical User Interface based Simple Calculator"""

# Importing tkinter module for creating GUI
from tkinter import *

root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=25, borderwidth=5)  #'Entry' used to take input field
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  #'grid' is used for positioning


# Function defined to take numbers as an input
def button_click(number):
    """To get the input number in the input field"""
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# Function for clearing the input field
def button_clear():
    """to clear the input field"""
    e.delete(0, END)


# Function to perform addition
def button_add():
    """Button used for addition"""
    first_number = e.get()
    global F_NUM
    global MATH
    MATH = "addition"
    F_NUM = int(first_number)
    e.delete(0, END)


# Function to carry out the operations
def button_equal():
    """Button used to evaluate the expression"""
    second_number = e.get()
    e.delete(0, END)
    if MATH == "addition":
        e.insert(0, F_NUM + int(second_number))
    if MATH == "subtraction":
        e.insert(0, F_NUM - int(second_number))
    if MATH == "multiplication":
        e.insert(0, F_NUM * int(second_number))
    if MATH == "division":
        e.insert(0, F_NUM / int(second_number))
    if MATH == "power":
        e.insert(0, F_NUM ** int(second_number))


# Function to perform subtraction
def button_subtract():
    """Button used to perform subtraction"""
    first_number = e.get()
    global F_NUM
    global MATH
    MATH = "subtraction"
    F_NUM = int(first_number)
    e.delete(0, END)


# Function to perform multiplication
def button_multiply():
    """Button used to perform Multiplication"""
    first_number = e.get()
    global F_NUM
    global MATH
    MATH = "multiplication"
    F_NUM = int(first_number)
    e.delete(0, END)


# Function to perform division
def button_divide():
    """Button used to perform Division"""
    first_number = e.get()
    global F_NUM
    global MATH
    MATH = "division"
    F_NUM = int(first_number)
    e.delete(0, END)


# Function for exponentiation
def button_pow():
    """Button used to perform Exponentiation"""
    first_number = e.get()
    global F_NUM
    global MATH
    MATH = "power"
    F_NUM = int(first_number)
    e.delete(0, END)


# defining the buttons
button_1 = Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=60, pady=20, command=lambda: button_click(0))


button_add = Button(root, text="+", padx=20, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=20, pady=20, command=button_equal)
button_clear = Button(root, text="AC", padx=20, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=20, pady=20, command=button_subtract)
button_multiply = Button(root, text="x", padx=20, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=20, pady=20, command=button_divide)
button_pow = Button(root, text="^", padx=20, pady=20, command=button_pow)


# positioning the buttons on the screen
button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)


button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)


button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)


button_0.grid(row=6, column=0, columnspan=2)
button_pow.grid(row=2, column=2)


button_add.grid(row=2, column=0)
button_subtract.grid(row=2, column=1)
button_equal.grid(row=6, column=2)


button_divide.grid(row=1, column=0)
button_multiply.grid(row=1, column=1)
button_clear.grid(row=1, column=2)

# terminating the continuous loop
root.mainloop()
