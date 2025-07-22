import streamlit as st
import joblib
import pandas as pd

# Load model and label encoder
model = joblib.load('crop_model.pkl')
le = joblib.load('crop_label_encoder.pkl')

# Set up page
st.set_page_config(page_title="🌾 Smart Crop Predictor", layout="centered", page_icon="🌿")
st.title("🌾 Smart Crop Recommendation System")
st.markdown("""
Welcome to the **AI-powered Crop Recommender**!  
Fill in the details below to get the most suitable crop for your region and season 🌱  
""")

st.markdown("---")

# Full list of Indian states (can expand based on training data availability)
indian_states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", 
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", 
    "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", 
    "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", 
    "West Bengal"
]

soil_types = ["Loamy", "Sandy", "Clay", "Red"]

# Interactive UI Components
col1, col2 = st.columns(2)

with col1:
    soil_input = st.selectbox("🧱 Select Soil Type", soil_types)
    soil_n = soil_types.index(soil_input)

with col2:
    state_input = st.selectbox("📍 Select Your State", indian_states)
    region = indian_states.index(state_input)  # Assume the model is trained to use indices

# Stylish sliders
rain = st.slider("🌧️ Average Rainfall (mm)", 0, 400, 200, help="How much rainfall does your land receive?")
temp = st.slider("🌡️ Average Temperature (°C)", 10, 45, 30, help="Ideal temperature during crop season?")
humi = st.slider("💧 Average Humidity (%)", 0, 100, 60, help="Relative humidity level in your area?")

st.markdown("---")

if st.button("🌿 Predict Best Crop", use_container_width=True):
    try:
        features = [[soil_n, region, rain, temp, humi]]
        prediction = model.predict(features)[0]
        crop_name = le.inverse_transform([prediction])[0]

        # Display prediction
        st.success(f"✅ **Recommended Crop**: `{crop_name}` 🌱")

        # Explainability mock (you can improve this with actual SHAP or rule-based explanation)
        explanation = f"""
### 🧐 Why **{crop_name}** is Recommended?
- **Soil Type**: {soil_input} is ideal for {crop_name}'s root development.
- **State**: In {state_input}, this crop is commonly grown in similar climate.
- **Rainfall**: {rain}mm matches the water requirement of {crop_name}.
- **Temperature**: {temp}°C provides an optimal growing condition.
- **Humidity**: {humi}% helps in efficient transpiration and disease resistance.

### ❌ Why Other Crops May Not Suit
Other crops might require:
- Different soil (e.g., Sandy instead of Loamy)
- More or less rainfall (e.g., 300mm+)
- Temperature beyond the current season’s capability
- Region-specific limitations or pest vulnerabilities
        """
        st.markdown(explanation)
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
