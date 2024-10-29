import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model.joblib")

# Title and description
st.title("Spotify Song Prediction")
st.write("Predict song popularity based on features.")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    predictions = model.predict(data)
    st.write("Predictions:", predictions)
