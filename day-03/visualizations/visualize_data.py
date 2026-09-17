import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../dataset/cleaned_facility_data.csv')
plt.style.use('default')
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# 1. Bar Chart: Avg Complaints by Location
sns.barplot(data=df, x='location', y='complaints', errorbar=None, ax=axes[0, 0])
axes[0, 0].set_title('Avg Complaints by Location')
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. Bar Chart: Count by Hygiene Risk
sns.countplot(data=df, x='hygiene_risk', ax=axes[0, 1])
axes[0, 1].set_title('Facility Count by Hygiene Risk')

# 3. Histogram: Cleanliness Score Distribution
sns.histplot(df['cleanliness_score'], bins=20, kde=True, ax=axes[0, 2])
axes[0, 2].set_title('Distribution of Cleanliness Scores')

# 4. Scatter Plot: Waste Level vs. Odor Score
sns.scatterplot(data=df, x='waste_level', y='odor_score', hue='hygiene_risk', alpha=0.6, ax=axes[1, 0])
axes[1, 0].set_title('Waste Level vs. Odor Score')

# 5. Additional Viz: Boxplot of Cleanliness by Facility Type
sns.boxplot(data=df, x='facility_type', y='cleanliness_score', ax=axes[1, 1])
axes[1, 1].set_title('Cleanliness Score by Facility Type')
axes[1, 1].tick_params(axis='x', rotation=45)

axes[1, 2].axis('off') # Hide empty subplot
plt.tight_layout()
plt.savefig('day3_visualizations.png')