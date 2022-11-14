# Core Packages
import streamlit as st

# Load EDA Packages
import pandas as pd
import numpy as np

# Load Data Visualize Packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')       # TkAgg
import seaborn as sns

# Func
def main():
    """All your code goes here"""
    st.title("Plotting with st.pyplot")
    df=pd.read_excel("/home/binp/Desktop/learn_streamlit/C0ExtFiles/iu_shcd.xlsx")
    st.dataframe(df.head())
    
if __name__ == '__main__':
    main()  