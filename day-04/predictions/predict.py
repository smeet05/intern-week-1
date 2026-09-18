import joblib
import numpy as np

# Load the saved scaler and model
scaler = joblib.load('../preprocessing/scaler.pkl')
model = joblib.load('../models/best_model.pkl')

# Example of a new facility inspection
# Features: [cleanliness_score, odor_score, waste_level, complaints, footfall, hours_since_cleaning]
new_facility_data = np.array([[3.5, 7.0, 85.0, 8, 500, 12.0]])

# Scale the data and predict
scaled_data = scaler.transform(new_facility_data)
prediction = model.predict(scaled_data)

print(f"The predicted hygiene risk for this facility is: {prediction[0]}") 
# (This should predict 'High')