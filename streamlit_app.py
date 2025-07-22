import streamlit as st
import joblib
import numpy as np
import pandas as pd
import datetime

# Load model and scaler
model = joblib.load("model/regression_model.pkl")
scaler = joblib.load("model/scaler.pkl")

st.title("🏃‍♂️ Half Marathon Finish Time Predictor")

# User inputs
anno = st.number_input("Year of Birth", min_value=1900, max_value=2025, value=1995)
km2025 = st.number_input("Kilometers run in last 4 month before the race", value=500)
pb5k = st.number_input("Personal Best 5K Time (in seconds)", value=1200)
total_km = st.number_input("Total Lifetime Kilometers", value=900)
sex = st.selectbox("Sex", ["Male", "Female"])
sesso_m = 1 if sex == "Male" else 0

# Prepare input
input_dict = {
    "ANNO": anno,
    "2025_km": km2025,
    "5K_PB": pb5k,
    "total_km": total_km,
    "SESSO_M": sesso_m,
}


input_dict["log_total_km"] = np.log(input_dict["total_km"])

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])
input_df = input_df[["ANNO", "2025_km", "5K_PB", "log_total_km", "SESSO_M"]]

# Predict
inputs_scaled = scaler.transform(input_df)
predicted_time = model.predict(inputs_scaled)[0]
predicted_time_str = str(datetime.timedelta(seconds=int(predicted_time)))

if st.button("Predict Finish Time"):
    st.success(f"🏁 Estimated Half Marathon Finish Time: {predicted_time_str}")
