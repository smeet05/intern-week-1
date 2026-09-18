import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# 1. Load the cleaned dataset
df = pd.read_csv('../dataset/cleaned_facility_data.csv')

# 2. Select the specific features requested for Day 4
features = ['cleanliness_score', 'odor_score', 'waste_level', 'complaints', 'footfall', 'hours_since_cleaning']
X = df[features]
y = df['hygiene_risk']

# 3. Train/Test Split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Feature Scaling (Standardization)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Save the preprocessed data and scaler for the next steps
joblib.dump((X_train_scaled, X_test_scaled, y_train, y_test), '../dataset/preprocessed_data.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("Preprocessing complete. Data and scaler saved.")