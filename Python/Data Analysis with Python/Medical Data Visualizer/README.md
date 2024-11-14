# Medical Data Visualizer

## Overview
The **Medical Data Visualizer** project aims to analyze and visualize medical examination data to uncover patterns related to cardiovascular disease. The project involves processing the data, creating visualizations for categorical features, and exploring correlations within the dataset.

## Purpose
The purpose of this project is to:

- Analyze medical examination data to gain insights into factors affecting cardiovascular health.
- Use data visualization to present insights related to cholesterol, glucose, and other medical measurements.
- Provide a better understanding of how different health metrics correlate with the presence of cardiovascular disease.

## Key Skills Demonstrated
1. **Data Cleaning and Transformation**
   - Added new calculated columns (e.g., `overweight`) and normalized existing values for analysis.

2. **Exploratory Data Analysis (EDA)**
   - Created visualizations for categorical medical data features to analyze differences between patients with and without cardiovascular disease.

3. **Correlation Analysis**
   - Generated a heatmap to visualize correlations between different medical metrics.

## Tools Used
- **Python**: Main programming language for data analysis and visualization.
- **Pandas**: Data manipulation and analysis.
- **Seaborn**: Visualization of categorical and correlation data.
- **Matplotlib**: Data visualization support.

## Project Components
1. **Data Import and Cleaning**
   - Imported the dataset `medical_examination.csv` using **Pandas**.
   - Created an `overweight` column based on BMI calculations and normalized `cholesterol` and `gluc` values.
   - Filtered out inconsistent or unrealistic data (e.g., diastolic pressure higher than systolic).

2. **Categorical Plot Creation**
   - Created a count plot for categorical features (`cholesterol`, `gluc`, `alco`, `active`, `smoke`) to compare distributions between patients with and without cardiovascular disease.

3. **Correlation Analysis**
   - Generated a correlation matrix heatmap to visualize relationships between different health metrics.

## Getting Started
To run the project:

1. Ensure you have **Python** installed along with the required libraries: **Pandas**, **Matplotlib**, and **Seaborn**.
2. Download the dataset `medical_examination.csv` and place it in the same directory as the script.
3. Run the script `medical_data_visualizer.py` to generate the visualizations:
   - Categorical plot.
   - Correlation heatmap.

## Notes
This project provides insights into medical data through the use of visual analytics, helping to better understand factors that may contribute to cardiovascular health issues. It demonstrates data cleaning, transformation, and visualization techniques applied to a health-related dataset.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for collaboration or if you have any questions about this project.
