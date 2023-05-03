import tkinter as tk

root = tk.Tk()

root.geometry ("250x100")
root.title("columnspan")

l1 = tk.Label(root, text='First', width=20)
l1.grid(row=1, column=1)

l2 = tk.Label (root, text='Second', width=20)
l2.grid(row=1, column=2)

l3 = tk.Label(root, text='Both First and Second, columnspan=2', background="red")
l3.grid(row=2, column=1, columnspan=2)
root.mainloop()