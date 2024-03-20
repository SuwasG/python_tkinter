from tkinter.simpledialog import askfloat
from tkinter import * 
from tkinter import messagebox 

top = Tk()
top.geometry('500x100') # w x(small x) h

def show():
    num = askfloat("Input", "Input a float")
    print(num)

b = Button(top, text ="Click", bg="red", fg="blue", command=show())
b.place(x=50, y=50)
top.mainloop()