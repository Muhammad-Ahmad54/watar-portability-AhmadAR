import joblib
import streamlit as st
import numpy as np

# Load the saved Random Forest model
model = joblib.load('random_forest_model.joblib')

# App title
st.title("Water Potability Prediction")

# Input features
ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
hardness = st.number_input("Hardness", min_value=0.0)
solids = st.number_input("Solids", min_value=0.0)
chloramines = st.number_input("Chloramines", min_value=0.0)
sulfate = st.number_input("Sulfate", min_value=0.0)
conductivity = st.number_input("Conductivity", min_value=0.0)
organic_carbon = st.number_input("Organic Carbon", min_value=0.0)
trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0)
turbidity = st.number_input("Turbidity", min_value=0.0)

# Predict button
if st.button("Predict Potability"):
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon, trihalomethanes, turbidity]])

    # Make prediction using Random Forest with RandomOverSampler model
    prediction = model.predict(input_data)[0]

    result = "Safe to Drink" if prediction == 1 else "Not Safe to Drink"
    st.success(f"Prediction: {result}")