from operator import eq

from sympy import symbols, Integral, S
import streamlit as st

def integral():
    st.title("Integral Solver")
    st.write("You have chosen to solve integrals.")
    st.write("Please enter the function you want to integrate (use 'x' as the variable):")
    st.text_input("Function f(x):", key="func_input")
    st.text_input("Lower limit (leave blank for indefinite integral):", key="lower_limit_input")
    st.text_input("Upper limit (leave blank for indefinite integral):", key="upper_limit_input")
    st.button("Calculate Integral", args=())

    st.write(f"The integral result will be displayed here.")
    x = symbols('x')
    func_input = st.session_state["func_input"]
    lower_limit_input = st.session_state["lower_limit_input"]
    upper_limit_input = st.session_state["upper_limit_input"]


    try:
        func = eq(func_input, x)
        if lower_limit_input and upper_limit_input:
            lower_limit = S(lower_limit_input)
            upper_limit = S(upper_limit_input)
            integral_result = Integral(func, (x, lower_limit, upper_limit)).doit()
        else:
            integral_result = Integral(func, x).doit()

        st.write(f"The integral of f(x) is: {integral_result}")
    except Exception as e:
        st.write(f"An error occurred: {e}")
