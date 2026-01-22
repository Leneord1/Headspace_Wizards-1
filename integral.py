import sympy as sym

def integral():

    from sympy import symbols, Integral, S

    x = symbols('x')

    print("You have chosen integrals.")
    print("Please enter the function you want to integrate (use 'x' as the variable):")
    func_input = input("f(x) = ")
    print("Please enter the variable of integration (default is 'x'):")
    var_input = input("Variable of integration: ").strip()
    if var_input == '':
        var_input = 'x'
    var = symbols(var_input)

    try:
        func = S(func_input)

        integral_result = Integral(func, var).doit()
        print(f"The integral of f(x) with respect to {var_input} is: {integral_result} + C")
    except Exception as e:
        print(f"An error occurred: {e}")