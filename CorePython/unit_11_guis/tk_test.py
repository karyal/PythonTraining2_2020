from tkinter import *
from PIL import Image, ImageTk
frame =Tk()
frame.title('HOME')
frame.geometry("250x250")
photo = ImageTk.PhotoImage(file="icon.png")
frame.iconphoto(False,photo)
frame.mainloop()