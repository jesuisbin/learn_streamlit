# Core Packages
import streamlit as st

# Text Input
fname = st.text_input("Enter Firstname",max_chars=15)
# Text Input Hide Password
password = st.text_input("Enter Password",type='password')
st.title(fname)

# Text Area
message = st.text_input("Enter Message")
st.write(message)

# Numbers
number = st.number_input("Enter Number")

# Date Input
myappointment = st.date_input("Appointment")

# Time Input
mytime = st.time_input("My Time")

# Color Picker
color = st.color_picker("Select Colour")