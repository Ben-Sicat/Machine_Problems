    from math import *
    import re
    class Calculator:


        #change the self to equation when testing function in this file
        
            
        def bisection(equation, a, b,maxiter, tol=1e-6 ):
            

            # Convert the equation string to a lambda function that can be evaluated.
            equation = re.sub(r"(\d)x", r"\1*x", equation)
            equation = equation.replace("^", "**")
            #lambda cant be evaluated in ui.pu
            equation = eval("lambda x: " + equation)

            # Check if the interval [a, b] contains a root.
            if equation(a) * equation(b) >= 0:
                return None

            # Perform the bisection method until the root is found or the maximum number of iterations is reached.
            for i in range(maxiter):
                c = (a + b) / 2
                if abs(equation(c)) < tol:
                    print(f"Found a root of the equation: {c:.20f}")
                    return c
                elif equation(c) * equation(a) < 0:
                    b = c
                else:
                    a = c
                print(f"Iteration {i+1}: current approximation = {c:.20f}")
            return None

        # Example usage:
        # equation_str = input("Enter a mathematical equation in x: ")
        # a = float(input("Enter the lower bound of the interval: "))
        # b = float(input("Enter the upper bound of the interval: "))

        # root = bisection(equation_str, a, b)
        # if root is None:
        #     print("No root was found within the maximum number of iterations.")
        # else:
        #     print(f"A root of the equation is: {root}")


        def secant(self, x0, x1, tol=1e-6, maxiter=100):
            # Convert the equation string to a lambda function that can be evaluated.
            equation = re.sub(r"(\d)x", r"\1*x", self.equation)
            equation = equation.replace("^", "**")
            equation = eval("lambda x: " + equation)

            # Perform the secant method until the root is found or the maximum number of iterations is reached.
            fx0 = equation(x0)
            fx1 = equation(x1)
            for i in range(maxiter):
                x = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
                fx = equation(x)
                if abs(fx) < tol:
                    print(f"Found a root of the equation: {x:.20f}")
                    return x
                x0 = x1
                fx0 = fx1
                x1 = x
                fx1 = fx
                print(f"Iteration {i+1}: x = {x:.20f}, f(x) = {fx:.20f}")
            print("Reached the maximum number of iterations.")
            return None
        def run(self):
            equation = self.equation
            res = self.bisection(equation, -10, 10)
            return res
        # Example usage of secant function
        # equation = "x-cos(x)"
        # x0 = -10
        # x1 = 10
        # tol = 1e-6
        # maxiter = 100

        # root = secant(equation, x0, x1, tol, maxiter)
        # print(root)


