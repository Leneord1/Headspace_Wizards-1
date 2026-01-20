import streamlit as st
# Streamlit page configuration
st.set_page_config(page_title="My Basic Streamlit Page", layout="wide")
st.title("Welcome to My Basic Streamlit Page")
st.write("This is a simple Streamlit application.")
st.header("This is my first basic Streamlit app")
st.write("You can add just about any kind of data using `st.write()`.")
st.subheader("Here's a subheader")
st.write("You can also create dataframes and display them:")
# Add a data table (example using pandas)


# Add a button
if st.button("Click me!"):
    st.write("Button clicked!")