import tkinter as tk
from math import *
import re

class Calculator:
    @staticmethod
    def bisection(equation, a, b, tol, maxiter=100):
        # Convert the equation string to a lambda function that can be evaluated.
        equation = re.sub(r"(\d)x", r"\1*x", equation)
        
        equation = equation.replace("^", "**")
        equation = eval("lambda x: " + equation)

        # Check if the interval [a, b] contains a root.
        if equation(a) * equation(b) >= 0:
            return None, []

        # Perform the bisection method until the root is found or the maximum number of iterations is reached.
        results = []
        for i in range(maxiter):
            c = (a + b) / 2
            fx = equation(c)
            results.append(( c, fx))
            if abs(fx) < tol:
                if(c > 0):
                    print(f"Found a root of the equation: xn = {c:.20f}")
                return c, results
            elif equation(c) * equation(a) < 0:
                b = c
            else:
                a = c
        return None, results

    
    @staticmethod
    def secant(equation, x0, x1, tol,maxiter = 100):
        # Convert the equation string to a lambda function that can be evaluated.
        equation = re.sub(r"(\d)x", r"\1*x", equation)
        equation = equation.replace("^", "**")
        equation = eval("lambda x: " + equation)

        # Perform the secant method until the root is found or the maximum number of iterations is reached.
        fx0 = equation(x0)
        fx1 = equation(x1)
        results = []
        for i in range(maxiter):
            x = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            fx = equation(x)
            results.append((x, fx))
            if abs(fx) < tol:
                print(f"Found a root of the equation: x = {x:.20f} ")
                return x, results, fx
            x0 = x1
            fx0 = fx1
            x1 = x
            fx1 = fx
        print("Reached the maximum number of iterations.")
        return None, results, None


def execute():
    fx = str(fx_textbox.get())
    a = float(a_textbox.get())
    b = float(b_textbox.get())
    tol = float(tol_textbox.get())
    result, bisection_results = Calculator.bisection(fx, a, b, tol)
    res, secant_results, fx = Calculator.secant(fx, a, b, tol)
    lb.delete(0, tk.END)
    if result is not None:
        lb.insert(tk.END, f"Found a root of the equation using bisection method: {result:.20f} ")
        lb.insert(tk.END, "Iterations (bisection method):")
        for iteration, (c, fx) in enumerate(bisection_results):
            lb.insert(tk.END, f"Iteration {iteration}: c = {c:.20f}, f(c) = {fx:.20f}")
        lb.insert(tk.END, "")
    else:
        lb.insert(tk.END, "Could not find a root of the equation using bisection method.")
    if res is not None:
        lb.insert(tk.END, f"Found a root of the equation using secant method: {res:.20f}")
        lb.insert(tk.END, f"f({res:.20f}) = {fx:.20f}")
        lb.insert(tk.END, "Iterations (secant method):")
        for i, (x, fx) in enumerate(secant_results):
            lb.insert(tk.END, f"Iteration {i+1}: x = {x:.20f}, f(x) = {fx:.20f}")
        lb.insert(tk.END, "")
    else:
        lb.insert(tk.END, "Could not find a root of the equation using secant method.")


def reset_values():
    # Remove all items from the listbox
    lb.delete(0, tk.END)
    # Reset the text values of the textboxes
    fx_textbox.delete(0, tk.END)
    fx_textbox.insert(0, "")
    a_textbox.delete(0, tk.END)
    a_textbox.insert(0, "")
    b_textbox.delete(0, tk.END)
    b_textbox.insert(0, "")
    # max_textbox.delete(0, tk.END)
    # max_textbox.insert(0, "")


root = tk.Tk()
root.resizable(False, False)
root.title("Machine Problem 2")


# Create a f(x) label with a textbox
fx_label = tk.Label(root, text="f(x)")
fx_textbox = tk.Entry(root)

# Create an "a" label with a textbox
a_label = tk.Label(root, text="a")
a_textbox = tk.Entry(root)

# Create a "b" label with a textbox
b_label = tk.Label(root, text="b")
b_textbox = tk.Entry(root)

# Create a "max iterations" label with a textbox
# max_label = tk.Label(root, text="Max Iterations")
# max_textbox = tk.Entry(root)

tol_label = tk.Label(root, text="Tolerance")
tol_textbox = tk.Entry(root)

execute_button = tk.Button(root, text="Execute", command=execute)
reset_values_button = tk.Button(root, text="Reset Values", command=reset_values)

lb = tk.Listbox(root,width=80, height=50)


fx_label.grid(row=0, column=1)
fx_textbox.grid(row=0, column=2)
a_label.grid(row=1, column=0)
a_textbox.grid(row=1, column=1)
b_label.grid(row=1, column=2)
b_textbox.grid(row=1, column=3)
# max_label.grid(row=2, column=0)
# max_textbox.grid(row=2, column=1)
tol_label.grid(row=2, column=1)
tol_textbox.grid(row=2, column=2)
execute_button.grid(row=3, column=0,columnspan=2)
reset_values_button.grid(row=3, column=2,columnspan=2)

lb.grid(row=4, column=0, columnspan=4)


root.mainloop()