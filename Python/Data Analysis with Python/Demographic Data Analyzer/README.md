# Demographic Data Analyzer

## Overview
The **Demographic Data Analyzer** project is focused on analyzing census data to answer specific questions about demographics, such as average age, education levels, and income. The project uses **Pandas** for data manipulation and analysis, allowing us to draw insights from the dataset and present the results in a structured format.

## Purpose
The purpose of this project is to:

- Analyze demographic data from the census to answer key questions about race, education, and income.
- Use **Pandas** to efficiently manipulate and summarize data to extract meaningful insights.
- Understand the relationships between various demographic factors and income levels.

## Key Skills Demonstrated
1. **Data Loading and Cleaning**
   - Loaded census data from a CSV file and prepared it for analysis.

2. **Exploratory Data Analysis (EDA)**
   - Analyzed various demographic attributes to identify trends and distributions.

3. **Statistical Analysis**
   - Calculated specific statistics such as average age, percentage of people with certain education levels, and the distribution of salaries.

## Tools Used
- **Python**: Main programming language for data analysis.
- **Pandas**: Data manipulation and analysis for census data.

## Project Components
1. **Data Import**
   - Loaded the dataset `adult.data.csv` using **Pandas**.

2. **Data Analysis**
   - Calculated various statistics, including:
     - **Race Count**: Number of people of each race represented in the dataset.
     - **Average Age of Men**: Average age of male respondents.
     - **Percentage of Bachelor's Degree Holders**: Percentage of people with a Bachelor's degree.
     - **Income Analysis**: Percentage of people with advanced and non-advanced education earning more than 50K.
     - **Minimum Work Hours**: Minimum hours worked per week by any individual.
     - **Rich Percentage for Minimum Workers**: Percentage of people earning more than 50K among those working the minimum hours.
     - **Highest Earning Country**: Country with the highest percentage of people earning more than 50K.
     - **Top Occupation in India**: Most popular occupation for those earning more than 50K in India.

3. **Result Presentation**
   - Created a dictionary containing all calculated results and printed the dictionary for easy interpretation.

## Getting Started
To run the project:

1. Ensure you have **Python** installed along with **Pandas**.
2. Download the dataset `adult.data.csv` and place it in the same directory as the script.
3. Run the script `demographic_data_analyzer.py` to view the demographic analysis results.

## Example Output
```python
{
    "race_count": race_count,
    "average_age_men": 39.4,
    "percentage_bachelors": 16.4,
    "percentage_higher_education": 46.5,
    "percentage_lower_education": 17.4,
    "min_work_hours": 1,
    "rich_percentage": 10.0,
    "highest_earning_country": "United States",
    "highest_earning_country_percentage": 39.5,
    "top_IN_occupation": "Prof-specialty"
}
```
## Notes
This project demonstrates the use of Pandas for analyzing demographic data and extracting meaningful statistics. It highlights the power of Python for efficient data processing and provides insights into various socioeconomic factors affecting income.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for collaboration or if you have any questions about this project.