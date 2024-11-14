import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Import the data and set the index to the date column
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Task 2: Clean the data by filtering out outliers
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

# Task 3: Create a line chart
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='r', linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    return fig

# Task 4: Create a bar chart
def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.strftime('%B')
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    df_bar.plot(kind='bar', ax=ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.set_title("Average Daily Page Views for Each Month (2016-2019)")
    ax.set_xticklabels(range(2016, 2020), rotation=0)
    ax.legend(title="Months", labels=months)
    return fig

# Task 5: Create box plots
def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[0].set_title("Year-wise Box Plot (Trend)")
    
    sns.boxplot(x='month', y='value', data=df_box, order=months, ax=axes[1])
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    
    return fig

# Save and return the images
if __name__ == '__main__':
    draw_line_plot().savefig('line_plot.png')
    draw_bar_plot().savefig('bar_plot.png')
    draw_box_plot().savefig('box_plot.png')
