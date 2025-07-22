import numpy as np
import joblib
import pandas as pd
import datetime

model = joblib.load('Downloads/Portfolio/regression_model.pkl')
scaler = joblib.load('Downloads/Portfolio/scaler.pkl')
feature_order = ['ANNO', '2025_km', '5K_PB', 'log_total_km', 'SESSO_M']

def predict_half_marathon_finish_time(user_input_dict):

    # Predict half marathon finish time based on user input.
    #Parameters:
    #- user_input: List or array-like of features in the same order and format used during training:
    # ANNO, 2025_km, 5K_PB, log_total_km, SESSO_M

    input_df = pd.DataFrame([user_input_dict])

    if 'total_km' in input_df.columns:
        input_df['log_total_km'] = np.log(input_df['total_km'])
    
    missing = set(feature_order) - set(input_df.columns)
    if missing:
        raise ValueError(f"Missing required features: {missing}")
        
    input_df = input_df[feature_order]
    
    inputs_scaled = scaler.transform(input_df)

    pred_sec = model.predict(inputs_scaled)[0]
    return {
        'predicted_seconds': int(pred_sec),
        'formatted_time': str(datetime.timedelta(seconds=int(pred_sec)))}