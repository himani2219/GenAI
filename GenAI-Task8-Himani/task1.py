import streamlit as st

st.title("Welcome to Streamlit!")
name = st.text_input("Enter your name:")
button_clicked = st.button("Greet me")
if button_clicked:
    st.write(f"Hello, {name}!")