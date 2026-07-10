import streamlit as st
import pandas as pd
import numpy as np

# --- App Title and Description ---
st.title("My first streamlit app")
st.write("This is a simple Streamlit app to demonstrate basic functionality of Streamlit.")

# --- Interactive Widgets in the sidebar ---
st.sidebar.header("User Input Features")

# Text Input
user_name = st.sidebar.text_input("What is Your name?" , "Ganesh Khobragade")

#Slider
age = st.sidebar.slider("Select your age" , 0, 100, 25)

# Selecbox
favorite_color = st.sidebar.selectbox("What is your favorite colore ?", ["Blue","Green","Red","Yellow"])

# --- Main page content ---
st.header(f"Welcome, {user_name}!")
st.write(f"You are {age} years old and your favorite color is {favorite_color}.")

# --- Displaying Data ---
st.subheader("Here's some random data:")

# Create a simple DaataFrame
data = pd.DataFrame(
    np.random.randn(10, 5),
    columns= ('col %d' % i for i in range(5))

)

st.dataframe(data)

# --- Checkbox to show/hide content ---
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

# --- button to trigger an action ---
if st.button("Say hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye!")
    