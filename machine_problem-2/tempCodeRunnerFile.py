equation_str = input("Enter a mathematical equation in x: ")
    a = float(input("Enter the lower bound of the interval: "))
    b = float(input("Enter the upper bound of the interval: "))

    root = bisection(equation_str, a, b)
    if root is None:
        print("No root was found within the maximum number of iterations.")
    else:
        print(f"A root of the equation is: {root}")