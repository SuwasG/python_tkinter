import tkinter as tk 
window = tk.Tk()

frame1= tk.Frame(master=window , bg='green', width=100)
frame1.pack(fill=tk.X)

frame2= tk.Frame(master=window , bg='red', height=50)
frame2.pack(fill=tk.X)

frame3= tk.Frame(master=window , bg='orange', height=100)
frame3.pack(fill=tk.X)

frame4= tk.Frame(master=window , bg='blue', height=50)
frame4.pack(fill=tk.X)


frame5= tk.Frame(master=window , bg='green', height=100, width=200)
frame5.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame6= tk.Frame(master=window , bg='red', height=100, width=100)
frame6.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame7= tk.Frame(master=window , bg='blue', height=100, width=100)
frame7.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame8= tk.Frame(master=window , bg='violet', height=100, width=100)
frame8.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame8= tk.Frame(master=window , bg='magenta', height=100, width=100)
frame8.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)



window.mainloop()