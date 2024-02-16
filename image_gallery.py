from tkinter import *
from PIL import Image, ImageTk
import os, math

# function to get thumbnail images
def makeThumbs(imgdir, size=(100,100), subdir="thumbs"):
    thumbdir = os.path.join(imgdir, subdir)
    if not os.path.exists(thumbdir):
        os.mkdir(thumbdir)
    thumbs = []
    for imgFile in os.listdir(imgdir):
        if imgFile == subdir:  # Skip the subdir itself
            continue
        imgpath = os.path.join(imgdir, imgFile)
        if not os.path.isfile(imgpath):  # Skip if not a file
            continue
        thumbpath = os.path.join(thumbdir, imgFile)
        if os.path.exists(thumbpath):
            thumbobj = Image.open(thumbpath)
            thumbs.append((imgFile, thumbobj))
        else:
            print("making", thumbpath)
            try:
                imgobj = Image.open(imgpath)  # make new thumb
                imgobj.thumbnail(size, Image.ANTIALIAS)
                imgobj.save(thumbpath)
                thumbs.append((imgFile, imgobj))
            except Exception as e:
                print("Skipping...", imgpath, "Error:", e)
    return thumbs

# open an image in popup window
class ViewOne(Toplevel):
    def __init__(self, imgdir, imgFile):
        Toplevel.__init__(self)
        self.title(imgFile)
        imgpath = os.path.join(imgdir, imgFile)
       # Load the image using PIL
        img = Image.open(imgpath)
        # convert the PIL image to a format that can be used by Tkinter
        # imgobj = PhotoImage(file=imgpath)
        imgobj= ImageTk.PhotoImage(img)
        Label(self, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height()) # size in pixels
        self.savephotos = imgobj  # keep reference on me

    
    


# viewer function
def viewer(imgdir, kind=Toplevel, cols=None):
    win = kind()
    win.title("Viewer: " + imgdir)
    thumbs = makeThumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs))))  # fixed or NxN
    
    savephotos=[]

    for thumbsrow in [thumbs[i:i + cols] for i in range(0, len(thumbs), cols)]:
        row = Frame(win)
        row.pack(fill=BOTH)
        for (imgFile, imgobj) in thumbsrow:
            imgobj = Image.open(os.path.join(imgdir, "thumbs", imgFile))
            size = max(imgobj.size)  # width, height
            # Reload the image for display
            photo = ImageTk.PhotoImage(imgobj)
            link = Button(row, image=photo)
            link.image = photo  # keep a reference!
            handler = lambda savefile = imgFile:ViewOne(imgdir,savefile)
            link.config(command=handler, width=size, height=size)
            link.pack(side=LEFT, expand=YES)
            savephotos.append(photo)

    # creating exit button
    Button(win, text="Exit", command=win.quit, bg="red").pack(fill=X)

    return win, savephotos

if __name__ == "__main__":
    imgdir = "images"
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()
