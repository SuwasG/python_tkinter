from tkinter import * 
from tkinter import ttk 

top = Tk()

top.geometry('300x200')

frame =Frame(top)
frame.pack()

languages = ['python', 'sql', 'c', 'c++', 'c#', 'js', 'java', 'php']

cb=ttk.Combobox(frame, values=languages)
cb.set('choose any option: ')
cb.pack(padx=5, pady=5)

top.mainloop()