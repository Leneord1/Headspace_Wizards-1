import sympy as sym

def seriesExpansion():

    from sympy import symbols, series, S

    x = symbols('x')

    print("You have chosen series expansion.")
    print("Please enter the function you want to expand (use 'x' as the variable):")
    func_input = input("f(x) = ")
    print("Please enter the point about which to expand (default is 0):")
    point_input = input("Point: ").strip()
    if point_input == '':
        point_input = '0'
    print("Please enter the order of the expansion (default is 6):")
    order_input = input("Order: ").strip()
    if order_input == '':
        order_input = '6'

    try:
        func = S(func_input)
        point = S(point_input)
        order = int(order_input)

        series_result = series(func, x, point, order).removeO()
        print(f"The series expansion of f(x) about {point} up to order {order} is: {series_result}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return series_result