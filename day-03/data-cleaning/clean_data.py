import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_excel('../dataset/facility_hygiene_ml_dataset.xlsx', sheet_name='Facility Hygiene Dataset')

# 1. Remove Duplicates
df_clean = df.drop_duplicates().copy()

# 2. Handle Missing Values
# Impute numerical columns with the median
df_clean['cleanliness_score'] = df_clean['cleanliness_score'].fillna(df_clean['cleanliness_score'].median())
df_clean['waste_level'] = df_clean['waste_level'].fillna(df_clean['waste_level'].median())

# Impute categorical columns with the mode (most frequent value)
df_clean['water_availability'] = df_clean['water_availability'].fillna(df_clean['water_availability'].mode()[0])

# 3. Handle Outliers (Capping at the 99th percentile)
cap_footfall = df_clean['footfall'].quantile(0.99)
cap_hours = df_clean['hours_since_cleaning'].quantile(0.99)
df_clean['footfall'] = np.where(df_clean['footfall'] > cap_footfall, cap_footfall, df_clean['footfall'])
df_clean['hours_since_cleaning'] = np.where(df_clean['hours_since_cleaning'] > cap_hours, cap_hours, df_clean['hours_since_cleaning'])

# Save the cleaned dataset
df_clean.to_csv('../dataset/cleaned_facility_data.csv', index=False)