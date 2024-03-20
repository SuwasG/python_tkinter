from tkinter.simpledialog import askinteger
from tkinter import * 
from tkinter import messagebox 

top = Tk()
top.geometry('100x100') # w x(small x) h

def show():
    num = askinteger("Input", "Input an integer")
    print(num)

b = Button(top, text ="Click", command=show())
b.place(x=50, y=50)
top.mainloop()
