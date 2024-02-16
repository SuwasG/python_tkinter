from tkinter import *
from PIL import Image, ImageTk

root =Tk() # object of Tk() class.

# gui logic here
# width x height
root.geometry("733x434")
# width, height
root.minsize(300, 100)
# width, height
root.maxsize(1200, 900)
# images
# photo = PhotoImage(file="images/camera.jpg") # supports only for png images.

# for jpg images
image = Image.open("images/camera.jpg")
photo = ImageTk.PhotoImage(image)

# label
label = Label(root, text="This is python GUI", image=photo)
label.pack()


# event loop
root.mainloop()
