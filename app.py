import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("iris_data_model")

st.title("Iris Flower Classification App")
st.write("Enter the flower measurements to predict the species.")

# User input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Prediction button
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Species: {prediction[0]}")
