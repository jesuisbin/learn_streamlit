# Basics & Fundamentals

# Core Packages
import streamlit as st

# Load EDA Packages
import pandas as pd

# Display Data
df=pd.read_excel("/home/binp/Desktop/learn_streamlit/C0ExtFiles/iemthesis_sem2-2021.xlsx")

# Method 1
st.dataframe(df)

# Adding a colour style from pandas
# Highlight giá trị lớn nhất trong df (int or float)
# st.dataframe(df.style.highlight_max(axis=0))

# # Method 2: Static Table
# st.table(df.head())

# Method 3: Using superfunc st.write
st.write(df.head())

# Display Json
st.json({'data':'name'})

# Display Code
mycode = """"
def sayhi():
    print("Hello Streamlit")
end
"""
st.code(mycode,language='python')    