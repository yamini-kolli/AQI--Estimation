import streamlit as st
import pandas as pd

st.title("Recent Estimations")
st.markdown("---")

dataframe = pd.read_csv('results/recent_estimates.csv')
st.dataframe(dataframe)