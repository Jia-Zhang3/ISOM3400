import streamlit as st

st.title("Welcome to Streamlit!")

st.write("Hello, Streamlit!")
st.write(12345)
st.write({"Name": "Alice", "Age": 30})

st.write("**Bold Text** and *Italic Text*")

st.header("Section 1: Introduction")

age = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)
st.write(f"Your age is {age}")

option = st.selectbox("Choose your favorite color:",
                      ["Red", "Blue", "Green"])
st.write(f"You selected: {option}")

if st.button("Click Me"):
    st.write("Button clicked!")
  
st.success("Operation completed successfully!")

import streamlit as st

st.title("Streamlit Demo App")
st.header("User Input Section")

st.write("Please provide your details below:")

age = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)
color = st.selectbox("Choose your favorite color:",
                     ["Red", "Blue", "Green"])

if st.button("Submit"):
    st.success(f"Thank you! Age: {age}, Favorite Color: {color}")
