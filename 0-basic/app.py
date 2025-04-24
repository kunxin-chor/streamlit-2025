# add new functionality to a python program via what is known as a package or a library
# const st = require('streamlit')
# import st from 'streamlit'
import streamlit as st 

st.title("Hello from Streamlit")

st.header("Welcome to my first streamlit app")

st.write("The quick brown fox jumps over the lazy dog")

# Streamlit is an immediate mode GUI
# The GUI is reran either at a fixed interval OR when a change is detected in the UI
name = st.text_input("Please enter your name")
st.write("Hello " + name)
