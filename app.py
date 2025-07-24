import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("Simple House Price Predictor")

# Training data
X = np.array([[50], [60], [70], [80], [90]])
y = np.array([150, 180, 210, 240, 270])

model = LinearRegression()
model.fit(X, y)

# User input
size = st.number_input("Enter house size in square meters:", min_value=10, max_value=1000, value=75)
predicted_price = model.predict(np.array([[size]]))[0]

st.write(f"💰 Predicted price: €{predicted_price:.2f}k")
