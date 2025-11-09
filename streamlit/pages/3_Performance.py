import streamlit as st
import pandas as pd

st.title("Model Selection & Evalution")
st.markdown('---')

st.text('Performance of Models on Trainning Data:')
train_results = pd.read_csv('results/results_train.csv')
st.dataframe(train_results)

st.text('Performance of Models on Testing Data:')
test_results = pd.read_csv('results/results_test.csv')
st.dataframe(test_results)