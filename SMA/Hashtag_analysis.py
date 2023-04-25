# Exp 4

'''
To determine which hashtags are most popular among different user groups, we can use the following approach:

- Read in the CSV file containing the social media data and filter it to include only the columns we need (e.g. user ID, user group, and hashtags).
- Split the hashtags into individual words and count their frequency for each user group.
- Plot the top N most frequent hashtags for each user group in a bar chart.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Read in the CSV file
df = pd.read_csv('hashtag_analysis.csv')

# Group the data by hashtags and user groups, and count the occurrences
hashtags_by_group = df.groupby(
    ['user_group', 'hashtags']).size().reset_index(name='count')

# Plot a horizontal bar chart for each user group
for group in df['user_group'].unique():
    group_data = hashtags_by_group[hashtags_by_group['user_group'] == group].sort_values('count', ascending=False).head(10)
    ax = group_data.plot(kind='barh', x='hashtags', y='count',
                         legend=False, title=f'Top Hashtags for {group}')
    ax.set_xlabel('Frequency')
    plt.tight_layout()
    plt.show()

'''
for i,row in dataset.iterrows():
    loc_data = ast.literal_eval(row['additional_data'])
    hashtags = [token for token in row.tweet.split() if token.startswith('#')]
    dataset['Hashtags'][i] = hashtags

    if loc_data['place']:
        dataset['Country'][i] = loc_data['place']['country']
'''
