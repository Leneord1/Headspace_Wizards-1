from turtledemo.forest import doit1
import matplotlib.pyplot as plt
from sympy import symbols
from sympy import Limit, S
from sympy import sympify
import streamlit as st

def limits():
    # Streamlit limits setup
    st.title("Limits Solver")
    st.write("You have chosen to solve limits.")
    st.write("Please enter the function, the point to which x approaches, and the direction of the limit.")
    st.text("Use 'x' as the variable in your function.")
    st.text_input("Function f(x):", key="func_input")
    st.text_input("Point to which x approaches:", key="point_input")
    st.text_input("Direction of the limit ('+' for right-hand, '-' for left-hand, leave blank for both sides):", key="direction_input")


    x = symbols('x')

    # Retrieve inputs from Streamlit session state
    func_input = st.session_state["func_input"]
    point_input = st.session_state["point_input"]
    direction_input = st.session_state["direction_input"]
    st.button("Calculate Limit", on_click=calculate_limit(func_input, point_input, direction_input, x), args=(func_input, point_input, direction_input, x))


def calculate_limit(func_input, point_input, direction_input,x):
    try:
        func = S(func_input)
        point = S(point_input)

        if direction_input == '+':
            limit_result = Limit(func, x, point, dir='+').doit()
        elif direction_input == '-':
            limit_result = Limit(func, x, point, dir='-').doit()
        else:
            limit_result = Limit(func, x, point).doit()

        st.write(f"The limit of f(x) as x approaches {point} is: {limit_result}")
        st.pyplot(limit_result)
        plt.savefig("my_figure.png")
    except Exception as e:
        st.write(f"An error occurred: {e}")