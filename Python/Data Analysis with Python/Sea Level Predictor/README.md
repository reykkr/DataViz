# Sea Level Predictor

## Overview
The **Sea Level Predictor** project is a data science analysis and visualization project focused on predicting the rise in sea levels based on historical data. The analysis includes creating a scatter plot of the sea level data and calculating lines of best fit to make future predictions.

## Purpose
The purpose of this project is to:

- Analyze historical sea level data and predict future sea level rise through linear regression.
- Visualize the results with clear and informative plots to communicate the trends effectively.

## Key Skills Demonstrated
1. **Data Import and Cleaning**
   - Imported historical sea level data using **Pandas**.

2. **Exploratory Data Analysis (EDA)**
   - Created scatter plots to visualize historical data.

3. **Linear Regression**
   - Used **SciPy** to calculate lines of best fit for sea level predictions through the year 2050.

4. **Data Visualization**
   - Created plots using **Matplotlib** to effectively illustrate trends and predictions.

## Tools Used
- **Python**: Main programming language for data analysis and modeling.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib**: Visualization of sea level data and regression lines.
- **SciPy (linregress)**: Calculating linear regression for predicting future sea levels.

## Project Components
1. **Data Import and Cleaning**
   - Imported the dataset `epa-sea-level.csv` using **Pandas** for analysis.

2. **Scatter Plot Creation**
   - Created a scatter plot to visualize the historical rise in sea levels.

3. **Linear Regression Analysis**
   - Calculated a line of best fit for the entire dataset from 1880 to 2050.
   - Calculated a separate line of best fit for data from the year 2000 to predict trends through 2050.

4. **Visualization and Reporting**
   - Created a plot combining both regression lines with the historical scatter plot.
   - Saved the plot as `sea_level_rise.png` for further use.

## Getting Started
To run the project:

1. Ensure you have **Python** installed along with the required libraries: **Pandas**, **Matplotlib**, and **SciPy**.
2. Download the dataset `epa-sea-level.csv` and place it in the same directory as the script.
3. Run the script `sea_level_predictor.py` to generate the sea level rise visualization.

## Notes
This project aims to raise awareness about rising sea levels by visualizing historical data and predicting future trends. The analysis demonstrates the application of linear regression for environmental data to create future projections.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for collaboration or if you have any questions about this project.
