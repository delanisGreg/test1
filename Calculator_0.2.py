from tkinter import *

root = Tk()
root.title("Calculator")

Cal = Entry(root, width=65, borderwidth=5)
Cal.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    #
    current = Cal.get()
    Cal.delete(0, END)
    Cal.insert(0, str(current) + str(number))


def button_clear():
    Cal.delete(0, END)

def button_add():
    first_number = Cal.get()
    global f_num #save in |global| number, can use outside of this function
    global math
    f_num = int(first_number)
    math = "add"
    Cal.delete(0, END)


def button_subtract():
    first_number = Cal.get()
    global f_num
    global math
    f_num = int(first_number)
    math = "sub"
    Cal.delete(0, END)


def button_multiply():
    first_number = Cal.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "mul"
    Cal.delete(0, END)


def button_devide():
    first_number = Cal.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "dev"
    Cal.delete(0, END)


def button_equal():
    second_number = Cal.get()
    Cal.delete(0, END)
    if math == "add":
        Cal.insert(0, f_num + int(second_number))
    if math == "sub":
        Cal.insert(0, f_num - int(second_number))
    if math == "dev":
        Cal.insert(0, f_num / int(second_number))
    if math == "mul":
        Cal.insert(0, f_num * int(second_number))

#Define Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_subtraction = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiple = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_devide = Button(root, text="/", padx=41, pady=20, command=button_devide)
button_equal = Button(root, text="=", padx=88, pady=20, command=button_equal)
button_clear = Button(root, text="clear", padx=178, pady=20, command=button_clear)

#place buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_add.grid(row=3,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_subtraction.grid(row=2,column=3)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_multiple.grid(row=1,column=3)

button_0.grid(row=4,column=0)
button_equal.grid(row=4,column=1,columnspan=2)
button_devide.grid(row=4,column=3)
button_clear.grid(row=5,column=0,columnspan=4)

root.mainloop()