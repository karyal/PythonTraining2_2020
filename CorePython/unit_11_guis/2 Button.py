import tkinter as tk
from tkinter.font import Font
count = 1
def print_hello():
    global count
    print("You clicked on Button ->", count, " times")
    count=count+1

window = tk.Tk()
window.geometry("750x750")
button1 = tk.Button(window, text="Button 1", activebackground='red', activeforeground='blue', anchor=tk.CENTER)
button2 = tk.Button(window, text="Button 2", borderwidth=5, background='yellow')
button3 = tk.Button(window, bitmap='error')
button4 = tk.Button(window, text='Button 4', command = print_hello)
button5 = tk.Button(window, text='Button 5', cursor='plus')

button6 = tk.Button(window, text='Button 6', default=tk.NORMAL)
button7 = tk.Button(window, text='Button 7', default=tk.DISABLED)

button6 = tk.Button(window, text='Button 6', default=tk.NORMAL, foreground='green')
button7 = tk.Button(window, text='Button 7', default=tk.DISABLED, disabledforeground='red')

font1= Font(family='Helvetica',  size=36, weight='bold', slant='italic', underline=0, overstrike=0)
button8 = tk.Button(window, text='Button 8', default=tk.NORMAL, foreground='green', font=font1)

button9 = tk.Button(window, text='Button 9', height=2, width=30)

button10 = tk.Button(window, text='Button 10', highlightbackground='red', highlightcolor='green', highlightthickness=0)

image_file = tk.PhotoImage(file='button_1.gif')
button11 = tk.Button(window, text='Button 11', image=image_file)
button12 = tk.Button(window, text='How to show multiple text lines: tk.LEFT to left-justify each line; tk.CENTER to center them; or tk.RIGHT to right-justify.', width=45, height=4, justify=tk.RIGHT)
button13 = tk.Button(window, text='How to show multiple text lines: tk.LEFT to left-justify', overrelief=tk.RAISED, padx = 2, pady = 2)
button14 = tk.Button(window, text='Button 14', command = print_hello, relief = tk.RAISED, repeatdelay=500, repeatinterval=100)

button15 = tk.Button(window, text='Button 15', state = tk.NORMAL, takefocus=0)
button16 = tk.Button(window, text='Button 16', state = tk.NORMAL, takefocus=0)

v1 = tk.StringVar()
v1.set('Hello')
button17 = tk.Button(window, text='Button 17', state = tk.NORMAL, takefocus=0, textvariable=v1)
button18 = tk.Button(window, state = tk.NORMAL, takefocus=0, textvariable=v1, underline=4)

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()
button11.pack()
button12.pack()
button13.pack()
button14.pack()
button15.pack()
button16.pack()
button17.pack()
button18.pack()
window.mainloop()