import pandas as pd

df = pd.read_csv('../dataset/cleaned_facility_data.csv')

# Key Statistics
summary_stats = df.describe()
print(summary_stats)

# Insight 1: Correlation with complaints
correlations = df[['cleanliness_score', 'odor_score', 'waste_level', 'footfall', 'complaints']].corr()
print("\nCorrelations with Complaints:\n", correlations['complaints'].sort_values())

# Insight 2: Complaints by Location
location_complaints = df.groupby('location')['complaints'].mean().sort_values(ascending=False)
print("\nAverage Complaints by Location:\n", location_complaints)

# Insight 3: Cleanliness by Risk Level
risk_cleanliness = df.groupby('hygiene_risk')['cleanliness_score'].mean()
print("\nCleanliness Score by Risk:\n", risk_cleanliness)