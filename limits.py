def limits():
    from sympy import symbols, Limit, S

    x = symbols('x')

    print("You have chosen limits.")
    print("Please enter the function for which you want to find the limit (use 'x' as the variable):")
    func_input = input("f(x) = ")
    print("Please enter the point at which you want to find the limit (use 'oo' for infinity):")
    point_input = input("Limit as x approaches: ")

    try:
        func = S(func_input)
        if point_input == 'oo':
            point = S.Infinity
        elif point_input == '-oo':
            point = S.NegativeInfinity
        else:
            point = S(point_input)

        limit_result = Limit(func, x, point).doit()
        print(f"The limit of f(x) as x approaches {point_input} is: {limit_result}")
    except Exception as e:
        print(f"An error occurred: {e}")