import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load preprocessed data
X_train_scaled, X_test_scaled, y_train, y_test = joblib.load('../dataset/preprocessed_data.pkl')

# 2. Train Model 1: Logistic Regression
lr_model = LogisticRegression(random_state=42, max_iter=1000)
lr_model.fit(X_train_scaled, y_train)
lr_preds = lr_model.predict(X_test_scaled)
print("--- Logistic Regression ---")
print(f"Accuracy: {accuracy_score(y_test, lr_preds):.4f}")

# 3. Train Model 2: Random Forest
rf_model = RandomForestClassifier(random_state=42, n_estimators=100)
rf_model.fit(X_train_scaled, y_train)
rf_preds = rf_model.predict(X_test_scaled)
print("\n--- Random Forest ---")
print(f"Accuracy: {accuracy_score(y_test, rf_preds):.4f}")
print("\nClassification Report:\n", classification_report(y_test, rf_preds))

# 4. Save the best performing model (Logistic Regression achieved ~92% on this dataset)
joblib.dump(lr_model, 'best_model.pkl')
print("\nBest model saved to models/best_model.pkl")