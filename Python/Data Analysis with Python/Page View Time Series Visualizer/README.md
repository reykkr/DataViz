# Time Series Visualizer

## Overview
The **Time Series Visualizer** project is a data visualization project aimed at analyzing and visualizing forum page views from May 2016 to December 2019. The project involves creating line charts, bar charts, and box plots to uncover trends, seasonality, and other insights from the time series data.

## Purpose
The purpose of this project is to:

- Visualize time series data to identify trends, patterns, and seasonality.
- Use different chart types (line, bar, box) to present data in various informative formats.
- Provide insights into page view patterns on the FreeCodeCamp forum.

## Key Skills Demonstrated
1. **Data Import and Cleaning**
   - Imported time series data and filtered out outliers to ensure data quality.

2. **Time Series Visualization**
   - Created line plots to visualize overall trends over time.

3. **Bar Plot Analysis**
   - Created bar charts to show the average page views for each month, grouped by year.

4. **Box Plot Analysis**
   - Created box plots to illustrate the distribution of page views by year and by month to identify seasonal trends and variability.

## Tools Used
- **Python**: Main programming language for data analysis and visualization.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib**: Data visualization through line and bar plots.
- **Seaborn**: Box plots for detailed visual analysis.

## Project Components
1. **Data Import and Cleaning**
   - Imported the dataset `fcc-forum-pageviews.csv` using **Pandas** and set the date column as the index.
   - Filtered the dataset to remove outliers using quantiles to ensure accuracy.

2. **Line Plot Creation**
   - Created a line plot to visualize daily page views over the specified period.

3. **Bar Plot Creation**
   - Generated a bar plot to show the average daily page views for each month across the years 2016-2019.

4. **Box Plot Creation**
   - Created box plots to provide insights into the spread of page views across different years and months.

## Getting Started
To run the project:

1. Ensure you have **Python** installed along with the required libraries: **Pandas**, **Matplotlib**, and **Seaborn**.
2. Download the dataset `fcc-forum-pageviews.csv` and place it in the same directory as the script.
3. Run the script `time_series_visualizer.py` to generate the visualizations:
   - `line_plot.png`
   - `bar_plot.png`
   - `box_plot.png`

## Notes
This project demonstrates the application of time series data visualization techniques to understand trends and seasonality in forum page views. The visualizations generated offer insights into the variation in page views over time, including year-over-year and month-over-month trends.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for collaboration or if you have any questions about this project.
