# Day 4: Machine Learning - Hygiene Risk Prediction

## Project Overview
This project builds a machine learning pipeline to predict the `hygiene_risk` of a facility based on inspection metrics such as cleanliness score, odor score, waste levels, and complaints.

## Technology Stack
* Python
* Scikit-learn (Machine Learning modeling and evaluation)
* Pandas & Joblib (Data manipulation and serialization)

## ML Workflow Implemented
1. **Preprocessing**: Handled train/test splitting (80/20) and standardized numerical features using `StandardScaler`.
2. **Model Training**: Trained two classification models to compare performance.
3. **Evaluation**: Used Accuracy and Classification Reports (Precision, Recall, F1-score) to evaluate model performance.
4. **Prediction**: Saved the best model to generate predictions on unseen data.

## Model Comparison
* **Logistic Regression**: Achieved an accuracy of **91.9%**.
* **Random Forest**: Achieved an accuracy of **87.4%**.
* **Conclusion**: Logistic Regression outperformed Random Forest on this specific dataset, showing that a linear relationship handles the scaled numerical features slightly better for these specific risk thresholds.

## How to Run
1. `python -m pip install scikit-learn joblib pandas`
2. Run preprocessing: `cd preprocessing && python preprocess.py`
3. Train models: `cd ../models && python train_model.py`
4. Test predictions: `cd ../predictions && python predict.py`
5. Run the evaluation script: `cd ../evaluation && python evaluate.py`