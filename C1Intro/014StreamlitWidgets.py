# Core Packages
import streamlit as st

# Select/Multiple select
my_lang=["Python","C++","Julia"]

choice = st.selectbox("Language",my_lang)
st.write("You selected {}".format(choice))

# Multiple selection
spoken_lang=("English","French","Spanish")
my_spoken_lang=st.multiselect("Spoken Language",spoken_lang,default="English")

# Slider
# Numbers (Int/Float/Dates)
age=st.slider("Age",1,100)

# Any Datatype
# Select Slider
color = st.select_slider("Choose Colour",options=["red","yellow","blue","black","white"],value=("yellow","red"))
