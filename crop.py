import streamlit as st
import joblib

# Load model and label encoder
model = joblib.load('cropmodel.pkl')
le3 = joblib.load('crop_label_encoder.pkl')

st.set_page_config(page_title="Smart Crop Predictor", layout="centered")
st.title("🌾 Smart Crop Recommendation System")
st.markdown("Enter the details below to get the **best crop suggestion** for your land.")

# Input fields
soil_n = st.selectbox("🧱 Soil Type", options=[0, 1, 2, 3], format_func=lambda x: ["Loamy", "Sandy", "Clay", "Red"][x])
region = st.selectbox("📍 Region", options=[0, 1, 2, 3], format_func=lambda x: ["TamilNadu", "Punjab", "Gujarat", "Kerala"][x])
rain = st.slider("🌧️ Rainfall (mm)", min_value=0, max_value=400, value=200)
temp = st.slider("🌡️ Temperature (°C)", min_value=10, max_value=45, value=30)
humi = st.slider("💧 Humidity (%)", min_value=0, max_value=100, value=60)

if st.button("🌿 Predict Best Crop"):
    try:
        pred = model.predict([[soil_n, region, rain, temp, humi]])[0]
        crop_name = le.inverse_transform([pred])[0]
        st.success(f"✅ The best crop for farming is: **{crop_name}**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
