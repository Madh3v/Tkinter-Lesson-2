from tkinter import *

root = Tk()

Label(text="row=0, column=0", width=20).grid(row=0, column=0)
Label (text="row=0, column=1", width=20).grid(row=6, column=1)
Label (text="row=1, column=0", width=20).grid(row=1, column=0)
Label (text="row=1, column=1", width=20).grid(row=1, column=1)

root.mainloop()