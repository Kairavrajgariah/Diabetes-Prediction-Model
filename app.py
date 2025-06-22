from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle
import joblib
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
import os

app = Flask(__name__)

# Load the trained model and preprocessing components
def load_model():
    try:
        # Load the model and preprocessing components
        model = joblib.load('diabetes_model.pkl')
        scaler = joblib.load('scaler.pkl')
        return model, scaler
    except FileNotFoundError:
        return None, None

# Initialize model components
model, scaler = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        data = request.get_json()
        
        # Combine Systolic and Diastolic as a ratio for the model's BloodPressure input
        systolic = float(data['systolic'])
        diastolic = float(data['diastolic'])
        bp_ratio = systolic / diastolic if diastolic != 0 else 0
        features = [
            float(data['glucose']),
            float(data['bmi']),
            float(data['age']),
            bp_ratio  # Model uses Systolic/Diastolic ratio as BloodPressure
        ]
        
        # Create DataFrame with feature names
        columns = pd.Index(["Glucose", "BMI", "Age", "BloodPressure"])
        input_df = pd.DataFrame([features], columns=columns)
        
        # Apply preprocessing
        if scaler is not None and model is not None:
            # Scale the features
            scaled_features = scaler.transform(input_df)
            
            # Make prediction
            prediction_proba = model.predict_proba(scaled_features)[0]
            prediction = model.predict(scaled_features)[0]
            
            # Calculate risk percentage and convert to native Python types
            risk_percentage = float(prediction_proba[1] * 100)
            
            # Determine risk level
            if risk_percentage < 30:
                risk_level = "Low Risk"
                risk_color = "green"
            elif risk_percentage < 70:
                risk_level = "Medium Risk"
                risk_color = "orange"
            else:
                risk_level = "High Risk"
                risk_color = "red"
            
            return jsonify({
                'success': True,
                'prediction': int(prediction),
                'risk_percentage': round(risk_percentage, 2),
                'risk_level': risk_level,
                'risk_color': risk_color,
                'message': 'Prediction completed successfully!'
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Model not loaded. Please ensure model files are available.'
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error during prediction: {str(e)}'
        })

@app.route('/about')
def about():
    return render_template('about.html')

# For local development
if __name__ == '__main__':
    app.run(debug=True) 