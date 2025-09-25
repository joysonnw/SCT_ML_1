import streamlit as st
import joblib

model = joblib.load("house_price_model.pkl")

st.title("House Price Predictor")

sqft = st.number_input("Square Footage", min_value=500, max_value=10000, value=2000)
beds = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
baths = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

if st.button("Predict Price"):
    prediction = model.predict([[sqft, beds, baths]])[0]
    st.success(f"Predicted Price: ${prediction:,.2f}")

