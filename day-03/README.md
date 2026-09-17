# Day 3: Data Analysis & Visualization

## Project Overview
This project focuses on inspecting, cleaning, analyzing, and visualizing a real-world dataset containing facility hygiene records. The goal is to identify data quality issues and extract meaningful insights regarding hygiene risks and customer complaints.

## Technology Stack
* **Python**
* **Pandas** (Data manipulation and cleaning)
* **Matplotlib & Seaborn** (Data visualization)

## Project Structure
* `/dataset/`: Contains the original `facility_hygiene_ml_dataset.xlsx` and the output `cleaned_facility_data.csv`.
* `/data-cleaning/`: Contains `clean_data.py` which handles missing values, duplicates, and outliers.
* `/analysis/`: Contains `analyze_data.py` which generates statistical summaries and key insights.
* `/visualizations/`: Contains `visualize_data.py` which generates visual charts (`day3_visualizations.png`).

## How to Run
1. Ensure your virtual environment is active (if using one).
2. Install the required dependencies: `python -m pip install pandas openpyxl matplotlib seaborn`
3. Run the cleaning script: `cd data-cleaning && python clean_data.py`
4. Run the analysis script: `cd ../analysis && python analyze_data.py`
5. Run the visualization script: `cd ../visualizations && python visualize_data.py`

## Key Insights
1. **Complaint Drivers**: There is a strong negative correlation between cleanliness scores and complaints (-0.66), and a positive correlation between waste levels/odor scores and complaints (+0.59). 
2. **Location Hotspots**: The "Sitabuldi" location generates the highest average number of complaints (5.0 per facility) compared to the overall average.
3. **Risk Verification**: The assigned `hygiene_risk` labels align correctly with the data. Facilities labeled "Low" risk average a cleanliness score of 8.2, while "High" risk facilities average 4.6.

## Challenges Faced & Solutions
* **Challenge**: Encountered `ModuleNotFoundError: No module named 'pandas'` due to multiple Python environments on the machine.
* **Solution**: Bypassed the environment conflict by running the module-specific installation command `python -m pip install pandas openpyxl`.