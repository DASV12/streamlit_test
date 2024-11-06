import streamlit as st
from sklearn.datasets import load_iris

data = load_iris(as_frame=True)
df = data.frame

st.title("Example for Anyone AI")
st.header("Hello David Serna")
st.write(" afafa adfafaf ")
st.subheader(" Subheader")

st.dataframe(df)

# streamlit run app.py