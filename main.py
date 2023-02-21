import streamlit as st
import pandas as pd
import numpy as np


st.write("""
    # My First Streamlit Webpage

    and some more text
    """)

df = pd.read_csv('data.csv')
df

options = st.selection()

if(st.checkbox("Show Plotting Feature:")):
    sample_df = pd.DataFrame(
        np.random.randn(20, 3), columns=['a', 'b', 'c']
    )
    st.line_chart(sample_df)
    

myslider = st.slider("myslider")
st.write(2 * myslider)


