from tkinter import *

root = Tk()
root.title('Calculator')

erase = Entry(root, width=30, borderwidth=8, bg='white')
erase.grid(row=0, column=0, columnspan=3, padx=15, pady=15)
root['bg'] = 'gray'
root.resizable(False, False)


def button_clear():
    erase.delete(0, END)


def button_click(number):
    current = erase.get()
    erase.delete(0, END)
    erase.insert(0, str(current) + str(number))


def button_add():
    first_number = erase.get()
    global number
    global operation
    operation = 'addition'
    number = int(first_number)
    erase.delete(0, END)


def button_equal():
    second_number = erase.get()
    erase.delete(0, END)

    if operation == 'addition':
        erase.insert(0, number + int(second_number))

    if operation == 'subtraction':
        erase.insert(0, number - int(second_number))

    if operation == 'multiplication':
        erase.insert(0, number * int(second_number))

    if operation == 'division':
        if second_number == '0':
            erase.insert(0, 'Cannot divide by ZERO!')
        else:
            erase.insert(0, number / int(second_number))


def button_subtract():
    first_number = erase.get()
    global number
    global operation
    operation = 'subtraction'
    number = int(first_number)
    erase.delete(0, END)


def button_multiply():
    first_number = erase.get()
    global number
    global operation
    operation = 'multiplication'
    number = int(first_number)
    erase.delete(0, END)


def button_divide():
    first_number = erase.get()
    global number
    global operation
    operation = 'division'
    number = int(first_number)
    erase.delete(0, END)


button_1 = Button(root, text='7', padx=45, borderwidth=3, pady=25, command=lambda: button_click(7), bg='turquoise')
button_2 = Button(root, text='8', padx=45, borderwidth=3, pady=25, command=lambda: button_click(8), bg='turquoise')
button_3 = Button(root, text='9', padx=45, borderwidth=3, pady=25, command=lambda: button_click(9), bg='turquoise')
button_4 = Button(root, text='4', padx=45, borderwidth=3, pady=25, command=lambda: button_click(4), bg='turquoise')
button_5 = Button(root, text='5', padx=45, borderwidth=3, pady=25, command=lambda: button_click(5), bg='pink')
button_6 = Button(root, text='6', padx=45, borderwidth=3, pady=25, command=lambda: button_click(6), bg='turquoise')
button_7 = Button(root, text='1', padx=45, borderwidth=3, pady=25, command=lambda: button_click(1), bg='turquoise')
button_8 = Button(root, text='2', padx=45, borderwidth=3, pady=25, command=lambda: button_click(2), bg='turquoise')
button_9 = Button(root, text='3', padx=45, borderwidth=3, pady=25, command=lambda: button_click(3), bg='turquoise')
button_0 = Button(root, text='0', padx=45, borderwidth=3, pady=30, command=lambda: button_click(0), bg='red')

button_add = Button(root, text='+', padx=45, borderwidth=3, pady=30, command=button_add, bg='green')
button_equal = Button(root, text='=', padx=92, borderwidth=5, pady=27, command=button_equal, bg='yellow')
button_clear = Button(root, text='CLEAR', padx=79, borderwidth=5, pady=27, command=button_clear, bg='white')
button_subtract = Button(root, text='-', borderwidth=4, padx=45, pady=30, command=button_subtract, bg='green')
button_multiply = Button(root, text='*', borderwidth=4, padx=45, pady=30, command=button_multiply, bg='orange')
button_divide = Button(root, text='/', borderwidth=4, padx=45, pady=30, command=button_divide, bg='orange')

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
