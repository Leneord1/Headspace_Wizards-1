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
enter_button = st.button("Enter", key="enter_button")
if problem_type == "Derivative":
    derivative()
elif problem_type == "Integral":
    integral()
elif problem_type == "Limit":
    limits()
elif problem_type == "Series Expansion":
    seriesExpansion()
elif problem_type == "Graphing":
    graphing()