import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('medical_examination.csv')

# Task 1: Add an overweight column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Task 2: Normalize cholesterol and glucose values
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Task 3: Create a chart for categorical features
df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'alco', 'active', 'smoke'])
sns.catplot(x='variable', hue='value', col='cardio', kind='count', data=df_cat)

# Task 4: Clean the data
df = df[(df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]

# Task 5: Create a correlation matrix
corr_matrix = df.corr()
mask = np.triu(corr_matrix)
sns.heatmap(corr_matrix, annot=True, fmt=".1f", cmap="
