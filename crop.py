<<<<<<< HEAD
import streamlit as st
import joblib

# Load model and label encoder
model = joblib.load('cropmodel.pkl')
le3= joblib.load('crop_label_encoder.pkl')

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
=======
import streamlit as st
import joblib
import random
import base64

# Load model and label encoder
model = joblib.load('crop_model.pkl')
le = joblib.load('crop_label_encoder.pkl')

# ---- Background image styling ----
def set_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_bg_from_local("assets/farm_bg.jpg")

# ---- Page settings ----
st.set_page_config(page_title="🌾 Smart Crop Predictor", layout="centered", page_icon="🌾")

# ---- App Logo ----
st.image("assets/logo.png", width=120)
st.markdown("<h1 style='text-align: center;'>🌿 Welcome to the Crop Predictor</h1>", unsafe_allow_html=True)

# ---- UI Selections ----
indian_states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", 
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", 
    "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", 
    "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", 
    "West Bengal"
]

soil_types = ["Loamy", "Sandy", "Clay", "Red"]

col1, col2 = st.columns(2)

with col1:
    soil_input = st.selectbox("🧱 Select Soil Type", soil_types)
    soil_n = soil_types.index(soil_input)

with col2:
    state_input = st.selectbox("📍 Select Your State", indian_states)
    region = indian_states.index(state_input)

# ---- Interactive Sliders with style ----
rain = st.slider("🌧️ Rainfall (mm)", 0, 400, 200, help="Your area's average seasonal rainfall")
temp = st.slider("🌡️ Temperature (°C)", 10, 45, 30, help="Season's average temperature")
humi = st.slider("💧 Humidity (%)", 0, 100, 60, help="Expected humidity level")

st.markdown("---")

# ---- On Predict Button ----
if st.button("🌿 Predict Best Crop", use_container_width=True):
    try:
        features = [[soil_n, region, rain, temp, humi]]
        prediction = model.predict(features)[0]
        crop_name = le.inverse_transform([prediction])[0]

        st.success(f"✅ **Recommended Crop**: `{crop_name}` 🌱")

        # Random logos for dynamic UI
        why_logos = ["assets/why1.png", "assets/why2.png", "assets/why3.png"]
        not_logos = ["assets/not1.png", "assets/not2.png", "assets/not3.png"]
        why_logo = random.choice(why_logos)
        not_logo = random.choice(not_logos)

        col3, col4 = st.columns([1, 3])
        with col3:
            st.image(why_logo, width=80)
        with col4:
            st.markdown(f"""
            ### ✅ Why **{crop_name}**?
            - **Soil**: {soil_input} is ideal for root development.
            - **State**: {state_input} supports large-scale {crop_name} farming.
            - **Rainfall**: {rain}mm aligns with {crop_name}'s water needs.
            - **Temperature**: {temp}°C ensures optimal growth.
            - **Humidity**: {humi}% avoids pests/disease for this crop.
            """)

        col5, col6 = st.columns([1, 3])
        with col5:
            st.image(not_logo, width=80)
        with col6:
            st.markdown(f"""
            ### ❌ Why Not Other Crops?
            - They might need different **soil types**.
            - Require **more/less rainfall** or different climate.
            - Unsuitable in **{state_input}** for current season.
            - Might be prone to **pest issues** at this humidity.
            """)

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
>>>>>>> 91b8cfd97d18ced647133867d1cc16de9492f143
