# import tkinter as tk
# from main import Calculator

# equation = ""

# # obj = Calculator(equation)

# def add_to_calculation(text):
#     global equation
#     equation += str(text)
#     text_result.delete("1.0", "end")
#     text_result.insert(tk.END, equation)
    
# def evaluate():
#     global equation, flag
    
#     obj = Calculator(equation)
    
#     # clear the equation and result fields
#     equation = ""
#     text_result.delete("1.0", "end")
    
#     # prompt for the lower bound and wait for input
#     if flag :
#         text_result.insert(tk.END, "Input Lower Bound")
#         root.wait_variable(text_result)
        
#     # read the lower bound input and clear the text field
#         a = float(text_result.get("1.0", "end"))
#         text_result.delete(1.0, "end")
#         flag = False
    
#     # prompt for the upper bound and wait for input
#     if not flag :
#         text_result.insert(tk.END, "Input Upper Bound")
#         root.wait_variable(text_result)
        
#         # read the upper bound input and clear the text field
#         b = float(text_result.get("1.0", "end"))
#         text_result.delete("1.0", "end")
        
#     # print(a, b)
#     # perform the bisection method and display the result
#     result = obj.bisection(a, b)
#     text_result.insert(tk.END, result)


# def clear_field():
#     global equation
#     equation = ""
#     text_result.delete("1.0", "end")
    
# def button(label):
#     return tk.Button(root, text=label, command=lambda: add_to_calculation(label), width = 4, font="Times 24")

# root = tk.Tk()
# root.geometry("800x400")


# text_result = tk.Text(root, height=2, width=48, font =("Times New Roman", 24) )
# text_result.grid(columnspan=5)
# button("1").grid(row=2, column=1,sticky="nsew")
# button("2").grid(row=2, column=2, sticky="nsew")
# button("3").grid(row=2, column=3, sticky="nsew")
# button("4").grid(row=3, column=1, sticky="nsew")
# button("5").grid(row=3, column=2, sticky="nsew")
# button("6").grid(row=3, column=3, sticky="nsew")
# button("7").grid(row=4, column=1, sticky="nsew")
# button("8").grid(row=4, column=2, sticky="nsew")
# button("9").grid(row=4, column=3, sticky="nsew")
# button("0").grid(row=5, column=2, sticky="nsew")
# button("x").grid(row=5, column=1, sticky="nsew")
# button("^").grid(row=5, column=3, sticky="nsew")
# button("+").grid(row=2, column=4, sticky="nsew")
# button("-").grid(row=3, column=4, sticky="nsew")
# button("*").grid(row=4, column=4, sticky="nsew")
# button("/").grid(row=5, column=4, sticky="nsew")
# button("(").grid(row=6, column=1, sticky="nsew")
# btn_c = tk.Button(root, text="C", command=clear_field, width = 4, font="Times 24")
# btn_c.grid(row=6, column=2, sticky="nsew")
# button(")").grid(row=6, column=3, sticky="nsew")
# flag = False
# btn_equal = tk.Button(root, text="=", command=evaluate, width = 4, font="Times 24")
# btn_equal.grid(row=6, column=4, sticky="nsew")
# button("cos").grid(row=2, column=0, sticky="nsew")
# button("sin").grid(row=3, column=0, sticky="nsew")
# button("tan").grid(row=4, column=0, sticky="nsew")
# button("log").grid(row=5, column=0, sticky="nsew")
# button("y").grid(row=6, column=0, sticky="nsew")




















# root.mainloop()