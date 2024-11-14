import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Task 1: Import the data from 'epa-sea-level.csv'
df = pd.read_csv('epa-sea-level.csv')

# Task 2: Create a scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(df['Year'],
            df['CSIRO Adjusted Sea Level'],
            label='Sea Level Data',
            c='blue',
            alpha=0.6)

# Task 3: Calculate and plot the line of best fit through 2050
slope, intercept, r_value, p_value, std_err = linregress(
    df['Year'], df['CSIRO Adjusted Sea Level'])

years = list(range(1880, 2051))
sea_level_pred = [slope * year + intercept for year in years]
plt.plot(years, sea_level_pred, label='Best Fit Line (1880-2050)', c='red')

# Task 4: Calculate and plot the line of best fit from 2000 to the most recent year through 2050
recent_data = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(
    recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

years_recent = list(range(2000, 2051))
sea_level_pred_recent = [
    slope_recent * year + intercept_recent for year in years_recent
]
plt.plot(years_recent,
         sea_level_pred_recent,
         label='Best Fit Line (2000-2050)',
         c='green')

# Set labels and title
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")

# Show legend
plt.legend()

# Save and return the image
plt.savefig('sea_level_rise.png')
