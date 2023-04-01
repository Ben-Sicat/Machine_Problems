import tkinter as tk
from main import *

equation = " "
obj = Calculator(equation)

def add_to_calculation(text):
    global equation
    equation += str(text)
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, equation)
    
def evaluate():
    global equation
    try:
        result = obj.bisection(equation, 0, 1)
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global equation
    equation = ""
    text_result.delete("1.0", tk.END)

root = tk.Tk()
root.geometry("500x480")

text_result = tk.Text(root, height=2, width=30, font =("Times New Roman", 24) )
text_result.grid(columnspan=5)


















root.mainloop()