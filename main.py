import sympy as sym
from probFinder import probFinder
from derivative import derivative
from integral import integral
from limits import limits
from seriesExpansion import seriesExpansion
from graphing import graphing
import streamlit as st

import pandas as pd
import numpy as np


# Streamlit app setup
st.title("Symbolic Mathematics Solver")
st.write("Choose the type of problem you want to solve:")
problem_type = st.selectbox(
    "Select Problem Type",
    ("Derivative", "Integral", "Limit", "Series Expansion", "Graphing")
)
enter_button = st.button("Enter", key="enter_button", help="Click to proceed to the selected problem type")

switcher = {
    "Derivative": derivative,
    "Integral": integral,
    "Limit": limits,
    "Series Expansion": seriesExpansion,
    "Graphing": graphing
}
if enter_button:
    func = switcher.get(problem_type, lambda: "Invalid input")()