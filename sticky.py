import tkinter as tk

root = tk.Tk()

root.geometry ("250x100")

root.title("sticky")

l1 = tk.Label(root, text='F Name (sticky=\'W\')' )
l1.grid(row=1,column=1,sticky="W")

el = tk.Entry(root, width=10,bg='yellow')
el.grid(row=1,column=2)

l2 = tk.Label(root, text='L Name (sticky=\'E\')')
l2.grid(row=2,column=1,sticky="E")

e2 = tk.Entry(root, width=10,bg='yellow')
e2.grid(row=2, column=2)

l3 = tk.Label(root, text='Add Door No and Street address')
l3.grid(row=3,column=1,sticky="W")

e3 = tk.Entry(root, width=10,bg='yellow')
e3.grid(row=3, column=2)

root.mainloop()