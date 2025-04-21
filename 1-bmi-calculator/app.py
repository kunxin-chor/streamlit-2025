import streamlit as st
st.title("BMI Calculator")


# the result will always be a number
# and the interface will enforce numeric input only
weight = st.number_input("Please enter your weight: ")
height = st.number_input("Please enter your height: ")

# choose imperial untis or the SI Units
# the second parameter of st.radio is a tuple
# a tuple is a list but with round brackets
# tuples are immutable (in other words, their values cnannot be changed)
unit = unit = st.radio("Select units of measurement", ("Imperial","Metric"))

# st.button will return True if it has been clicked
button_clicked = st.button("Calculate BMI")
if button_clicked:
    if unit == "Imperial":
        bmi = weight * 703 / (height **2)
    elif unit == "Metric":
        bmi = weight / height ** 2
    st.write("Your BMI is", bmi)

if weight > 0 and height > 0:
    bmi = weight / height ** 2
    st.write("BMI is ", bmi)