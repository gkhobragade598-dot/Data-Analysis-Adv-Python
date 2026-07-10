# import streamlit
import streamlit as st

#2. add a title to your app
st.title("My first streamlit app created by Prakash Senapati")

#3. add some text
st.write("Wellcone! This app calculates the square of a number.")

# 4. Create an interactive slider
st.header("Select a Number")
number = st.slider("Pick a number" , 0,10,100) # min, max, default

#5. Calculate and display the result
st.subheader("Result")
squared_number = number * number
st.write(f"The square of **{number}** is **{squared_number}**.")
