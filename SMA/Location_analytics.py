# Exp 2
'''
This program first loads the tweet data from a CSV file and removes any rows with missing values. It then creates a new column for the state abbreviation based on the location data by using a dictionary of state abbreviations and their full names, and a function that searches for these abbreviations in the location data.

Next, it plots the frequency of each state in the data using the Seaborn library. It creates a bar plot of the state frequencies using the state_counts DataFrame, and customizes the plot with labels and titles. The resulting plot shows the relative frequency of each state in the tweet data, which can help to identify where particular locations are most prevalent.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the tweet data from a CSV file
data = pd.read_csv("tweet_data.csv")

# Remove any rows with missing values
data = data.dropna()

# Create a new column for the state abbreviation based on the location data
states = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
    'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
    'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
}


def get_state(location):
    words = location.split()
    for word in words:
        if word.upper() in states:
            return states[word.upper()]
    return None


data['state'] = data['location'].apply(get_state)
print(data.head())

# Plot the frequency of each state in the data
state_counts = data['state'].value_counts()
# print("Count", state_counts)
plt.figure(figsize=(12, 6))

# name, values
sns.barplot(x=state_counts.index, y=state_counts.values, palette="rocket")
plt.xticks(rotation=90)
plt.xlabel('State')
plt.ylabel('Frequency')
plt.title('Frequency of States in Tweet Data')
plt.show()
