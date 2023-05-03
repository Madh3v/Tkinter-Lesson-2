import tkinter as tk

root = tk.Tk() 
root.title(" frames") 
top_frame= tk.Frame(root, width=100, height=100, bg="red") 
top_frame.grid(row=0, column=0, padx=10, pady=5)

tk.Label(top_frame, text="Top Frame").grid(row=0, column=0, padx=20, pady=5)
bottom_frame = tk.Frame(root, width=100, height=100, bg="green")

bottom_frame.grid(row=1, column=0, padx=10, pady=5)

tk.Label (bottom_frame, text="Bottom Frame").grid(row=1, column=0, padx=20, pady=5)
root.mainloop()