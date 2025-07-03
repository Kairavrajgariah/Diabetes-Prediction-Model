import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.combine import SMOTETomek
from xgboost import XGBClassifier

# Load the dataset
dataset = pd.read_csv('diabetes.csv')

# Use only the selected features
selected_features = ['Glucose', 'BMI', 'Age', 'BloodPressure']
x = dataset[selected_features]
y = dataset["Outcome"]

# Apply StandardScaler
sc = StandardScaler()
x_scaled = sc.fit_transform(x)

# Apply SMOTETomek for balancing
smt = SMOTETomek(random_state=42)
x_resampled, y_resampled = smt.fit_resample(x_scaled, y)

# Split the data (ensure 4 outputs)
x_train, x_test, y_train, y_test = train_test_split(
    x_resampled, y_resampled, test_size=0.2, random_state=42, stratify=y_resampled
)

# Train the XGBoost model
best_xgb = XGBClassifier(
    learning_rate=0.05,
    n_estimators=400,
    max_depth=6,
    min_child_weight=1,
    colsample_bytree=0.8,
    eval_metric='auc',
    random_state=42
)

best_xgb.fit(x_train, y_train, eval_set=[(x_test, y_test)], verbose=False)

# Save the model and preprocessing components
joblib.dump(best_xgb, 'diabetes_model.pkl')
joblib.dump(sc, 'scaler.pkl')

print("✅ Model and preprocessing components saved successfully!")
print("📁 Files created:")
print("   - diabetes_model.pkl")
print("   - scaler.pkl")

# Test the saved model
test_prediction = best_xgb.predict_proba(x_test[:1])[0]
print(f"\n🧪 Test prediction probability: {test_prediction}")
print("🎉 Model is ready for the web application!") 