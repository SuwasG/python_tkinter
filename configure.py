import tkinter as tk 
window = tk.Tk()

window.rowconfigure(0, minsize=60) # 0 means first row.
window.columnconfigure([0,1,2], minsize=50)

label1= tk.Label(text='A', bg="red", fg="white", padx=10, pady=5)
label2= tk.Label(text='B', bg="black", fg="white",padx=20, pady=20)
label3= tk.Label(text='C', bg="dodgerblue", fg="white")
label4= tk.Label(text='D', bg="orange", fg="black", padx=10, pady=20)

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)
label4.grid(row=1, column=0)

window.mainloop()