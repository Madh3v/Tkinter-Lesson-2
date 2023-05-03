import tkinter as tk

root = tk.Tk()

root.geometry ("250x100")

root.title("pad - padding")

l4 =tk.Label (root, text='padx=50,pady=50 ', borderwidth=2, relief='ridge')
l4.grid(row=2, column=2, ipadx=50, ipady=50)
root.mainloop()