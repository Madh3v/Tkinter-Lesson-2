import tkinter as tk

root = tk.Tk()

root.geometry ("250x100")
root.title("rowspan")

l1 = tk.Label(root, text='First', width=20)
l1.grid(row=0,column=1)

l2 = tk.Label(root, text='Second', width=20)
l2.grid(row=1, column=1)

l3 = tk.Label(root, text='Third', width=20)
l3.grid(row=2, column=1)

t1 = tk.Text(root, height=3, width=8, bg='yellow')
t1.grid(row=0, column=2, rowspan=3)
root.mainloop()