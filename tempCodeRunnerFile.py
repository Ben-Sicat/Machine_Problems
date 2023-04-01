def bisection(equation, a, b, tol=1e-6, maxiter=100):
   

#     # Convert the equation string to a lambda function that can be evaluated.
#     equation = re.sub(r"(\d)x", r"\1*x", equation)
#     equation = eval("lambda x: " + equation)

#     # Check if the interval [a, b] contains a root.
#     if equation(a) * equation(b) >= 0:
#         return None

#     # Perform the bisection method until the root is found or the maximum number of iterations is reached.
#     for i in range(maxiter):
#         c = (a + b) / 2
#         if abs(equation(c)) < tol:
#             return c
#         elif equation(c) * equation(a) < 0:
#             b = c
#         else:
#             a = c

#     return None

# # Example usage:
# equation_str = input("Enter a mathematical equation in x: ")
# a = float(input("Enter the lower bound of the interval: "))
# b = float(input("Enter the upper bound of the interval: "))

# root = bisection(equation_str, a, b)
# if root is None:
#     print("No root was found within the maximum number of iterations.")
# else:
#     print(f"A root of the equation is: {root}")