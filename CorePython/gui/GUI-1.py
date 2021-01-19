# https://docs.python.org/3/library/tkinter.html

from tkinter import *

"""
# Creating a new Window
frame = Tk() # Decalre and Initialize
frame.geometry("250x250")# Set Size
frame.title("My Window")
frame.mainloop() # Display Window

# Task-1
    # Set System Icon on Window

# Disable Resize (Window)
frame = Tk() # Decalre and Initialize
frame.geometry("250x250")# Set Size
frame.resizable(False, False)
frame.title("My Window")
frame.mainloop() # Display Window


# Solution of Task-1
frame = Tk() # Decalre and Initialize
frame.geometry("250x250")# Set Size
frame.resizable(False, False)
frame.title("My Window")

obj_icon = PhotoImage(file="icon.png")
frame.iconphoto(False, obj_icon)

frame.mainloop() # Display Window
"""
# Task-2
    # Label Control - Display message about control/user prompt
    # Text Box - Input Single Line Text
    # Multi-line Text Box - Comments
    # Radio Button - Single Selection from Options
    # Check Box - Multiple Selection from Options
    # Combo Box, List Box - Display Items
    # Button - Push-up Button (Event)

frame = Tk() # Decalre and Initialize
frame.geometry("250x250")# Set Size
frame.resizable(False, False)
frame.title("My Window")

obj_icon = PhotoImage(file="icon.png")
frame.iconphoto(False, obj_icon)

# Label Control
lbl_fn = Label(frame, text="Enter First No : ")
lbl_fn.place(x = 5, y = 2)

#Single Line Text Box
txt_n1 = Entry(frame)
txt_n1.place(x = 110, y = 2)

lbl_sn = Label(frame, text="Enter Second No : ")
lbl_sn.place(x = 5, y = 32)
txt_n2 = Entry(frame)
txt_n2.place(x = 110, y = 32)

# Button Control
btn_add = Button(frame, text=" ADD ")
btn_add.place(x=5, y=62)

frame.mainloop() # Display Window

# Task-2
    # Add click event on Button Class
    # Perform Addition