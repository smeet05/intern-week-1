import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# 1. Load Data & Preprocess (Requires facility_hygiene_ml_dataset.xlsx in the same folder)
df = pd.read_excel('facility_hygiene_ml_dataset.xlsx', sheet_name='Facility Hygiene Dataset')
df = df.drop_duplicates()
df['cleanliness_score'] = df['cleanliness_score'].fillna(df['cleanliness_score'].median())
df['waste_level'] = df['waste_level'].fillna(df['waste_level'].median())

# 2. Exploratory Data Analysis (EDA) Visualizations
os.makedirs('visualizations', exist_ok=True)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='hygiene_risk', y='cleanliness_score')
plt.title('Cleanliness Score Distribution by Hygiene Risk')
plt.savefig('visualizations/eda_risk_vs_cleanliness.png')

# 3. Feature Selection & Splitting
features = ['cleanliness_score', 'odor_score', 'waste_level', 'complaints', 'footfall', 'hours_since_cleaning']
X = df[features]
y = df['hygiene_risk']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Model Training (Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# 6. Evaluation
y_pred = model.predict(X_test_scaled)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# 7. Export Model and Scaler for the API
joblib.dump(model, '../backend/hygiene_model.pkl')
joblib.dump(scaler, '../backend/scaler.pkl')
print("Pipeline complete. Model and scaler saved to backend folder.")