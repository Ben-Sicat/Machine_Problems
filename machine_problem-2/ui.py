import tkinter as tk

root = tk.Tk()
root.geometry("500x480")

text_result = tk.Text(root, height=2, width=30, font =("Times New Roman", 24) )
text_result.grid(columnspan=5)
root.mainloop()