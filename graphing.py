from streamlit import status
import streamlit as st
import numpy as np
import matplotlib as plt
import time

def graphing():
    st.header("Graphing Module")
    st.write("This module will help you graph mathematical functions.")

    # Input function from user
    function_input = st.text_input("Enter a function of x (e.g., sin(x), x**2 + 3*x + 2):", "sin(x)")

    # Define the range for x
    x_min = st.number_input("Enter the minimum x value:", value=-10.0)
    x_max = st.number_input("Enter the maximum x value:", value=10.0)

    if st.button("Plot Function"):
        try:
            # Create an array of x values
            x = np.linspace(x_min, x_max, 400)

            # Evaluate the function safely
            y = eval(function_input)

            plt.figure(figsize=(10, 5))
            plt.plot(x, y, label=f'y = {function_input}')
            plt.title('Graph of the function')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.axhline(0, color='black',linewidth=0.5, ls='--')
            plt.axvline(0, color='black',linewidth=0.5, ls='--')
            plt.grid()
            plt.legend()
            st.pyplot(plt)
        except Exception as e:
            st.error(f"Error in plotting the function: {e}")