import streamlit as st
from rice_model import predict_rice_yield

st.set_page_config(page_title="Rice Yield Predictor", page_icon="🌾")

st.title("🌾 Rice Yield Potential Predictor")
st.markdown("Enter the soil and weather conditions to check if the yield potential is good.")

# User inputs
N = st.number_input("Nitrogen (N)", min_value=0.0, value=50.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, value=40.0)
K = st.number_input("Potassium (K)", min_value=0.0, value=40.0)
temperature = st.number_input("Temperature (°C)", value=25.0)
humidity = st.number_input("Humidity (%)", value=70.0)
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", value=100.0)

if st.button("Predict"):
    input_data = {
        'N': N, 'P': P, 'K': K,
        'temperature': temperature,
        'humidity': humidity,
        'ph': ph,
        'rainfall': rainfall
    }
    prediction = predict_rice_yield(input_data)
    st.success(f"🌾 Yield Potential: **{prediction}**")
