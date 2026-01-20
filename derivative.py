import sympy as sym

def derivative():

    from sympy import symbols, Derivative, S

    x = symbols('x')

    print("You have chosen derivatives.")
    print("Please enter the function you want to differentiate (use 'x' as the variable):")
    func_input = input("f(x) = ")

    try:
        func = S(func_input)

        derivative_result = Derivative(func, x).doit()
        print(f"The derivative of f(x) with respect to x is: {derivative_result}")
    except Exception as e:
        print(f"An error occurred: {e}")