import streamlit as st
st.title("Resturant Booking Website")

name = st.text_input("What is your name")

reservation_date = st.date_input("Reservation Date")

reservation_time = st.time_input("Reservation Time")

# outdoors or indoors
seating_preferences = st.radio("Seating preferences", ("Indoors", "Outdoors"))

# brunch, lunch or dinner
meal = st.selectbox("Which meal are you eating", (
    "Brunch",
    "Lunch",
    "Dinner"
))

# extra servcies - free flow drinks, birthday song, private room, open bar
extra_services = st.multiselect("Select extra services", ("Free Flow Drinks", "Birthday Song", "Private Room", "Open Bar"))

# checkboxes - booking terms and conditions
agree_terms = st.checkbox("Agree to the terms and conditions")

submitted = st.button("Submit", disabled=not agree_terms)
if submitted:
    st.html(f"""
        <ul>
            <li>Name: {name}</li>
            <li>Date: {reservation_date}</li>
            <li>Time: {reservation_time}</li>
            <li>Meal: {meal}</li>
            <li>Extra Services: {extra_services}</li>
        </ul>
    """)

