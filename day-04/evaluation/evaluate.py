import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load the preprocessed test data and the best model
# (We use '_' for the training variables because we only need the test data here)
_, X_test_scaled, _, y_test = joblib.load('../dataset/preprocessed_data.pkl')
model = joblib.load('../models/best_model.pkl')

# 2. Generate predictions on the test set
y_pred = model.predict(X_test_scaled)

# 3. Print required evaluation metrics
print("--- Model Evaluation Metrics ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")

# The classification report automatically calculates Precision, Recall, and F1-Score for each class
print("Detailed Classification Report (Precision, Recall, F1-Score):")
print(classification_report(y_test, y_pred))

# 4. Generate and save a Confusion Matrix visualization
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=model.classes_, 
            yticklabels=model.classes_)
plt.title('Confusion Matrix - Hygiene Risk Prediction')
plt.xlabel('Predicted Risk')
plt.ylabel('Actual Risk')

plt.tight_layout()
# Save the visual chart inside the evaluation folder
plt.savefig('confusion_matrix.png')
print("Confusion matrix visualization saved successfully as 'confusion_matrix.png'")