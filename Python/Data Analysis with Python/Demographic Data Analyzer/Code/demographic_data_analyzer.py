import pandas as pd

# Load the dataset
data = pd.read_csv(
    'adult.data.csv')  # Replace 'your_dataset.csv' with the actual file path

# Question 1: How many people of each race are represented in this dataset?
race_count = data['race'].value_counts()

# Question 2: What is the average age of men?
average_age_men = data[data['sex'] == 'Male']['age'].mean()

# Question 3: What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (data['education'] == 'Bachelors').mean() * 100

# Question 4: What percentage of people with advanced education make more than 50K?
advanced_education = ['Bachelors', 'Masters', 'Doctorate']
higher_education = data[data['education'].isin(advanced_education)]
percentage_higher_education = (higher_education['salary']
                               == '>50K').mean() * 100

# Question 5: What percentage of people without advanced education make more than 50K?
percentage_lower_education = (data[~data['education'].isin(advanced_education)]
                              ['salary'] == '>50K').mean() * 100

# Question 6: What is the minimum number of hours a person works per week?
min_work_hours = data['hours-per-week'].min()

# Question 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = data[data['hours-per-week'] == min_work_hours]
rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

# Question 8: What country has the highest percentage of people that earn >50K and what is that percentage?
country_stats = data[data['salary'] == '>50K']['native-country'].value_counts(
    normalize=True) * 100
highest_earning_country = country_stats.idxmax()
highest_earning_country_percentage = country_stats.max()

# Question 9: Identify the most popular occupation for those who earn >50K in India.
indian_occupation_stats = data[(data['native-country'] == 'India') & (
    data['salary'] == '>50K')]['occupation'].value_counts()
top_IN_occupation = indian_occupation_stats.idxmax()

# Rounding decimals to the nearest tenth
average_age_men = round(average_age_men, 1)
percentage_bachelors = round(percentage_bachelors, 1)
percentage_higher_education = round(percentage_higher_education, 1)
percentage_lower_education = round(percentage_lower_education, 1)
rich_percentage = round(rich_percentage, 1)
highest_earning_country_percentage = round(highest_earning_country_percentage,
                                           1)

# Output results as a dictionary
demographic_data = {
    "race_count": race_count,
    "average_age_men": average_age_men,
    "percentage_bachelors": percentage_bachelors,
    "percentage_higher_education": percentage_higher_education,
    "percentage_lower_education": percentage_lower_education,
    "min_work_hours": min_work_hours,
    "rich_percentage": rich_percentage,
    "highest_earning_country": highest_earning_country,
    "highest_earning_country_percentage": highest_earning_country_percentage,
    "top_IN_occupation": top_IN_occupation
}

# Print the results
print(demographic_data)
