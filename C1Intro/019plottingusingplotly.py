# Core Packages
import streamlit as st

# Load EDA Packages
import pandas as pd
import numpy as np

# Load Data Vis Pkg
import plotly.express as px

# Func
def main():
    """All your code goes here"""
    st.title("Plotting in Streamlit with Plotly")
    df=pd.read_excel("/home/binp/Desktop/learn_streamlit/C0ExtFiles/iu_shcd.xlsx")
    st.dataframe(df)
    
    fig=px.pie(df,values='Grade',names='Result',title='SHCD result IU')
    st.plotly_chart(fig)
    
    fig1=px.bar(df,y='Grade',x='Result')
    st.plotly_chart(fig1)
    
if __name__ == '__main__':
    main()