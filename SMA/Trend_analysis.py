# Exp 3

'''
In this example, the program reads in a CSV file with social media data and converts the 'date' column to a datetime data type using pd.to_datetime(). The 'date' column is then set as the index of the DataFrame using set_index().

Next, the data is resampled by month using the resample() method, and the number of entries in each month is counted using the count() method. The resulting monthly counts are plotted over time using matplotlib.

You can modify the program to read in your own CSV file with time data associated with social media.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Read in the CSV file
df = pd.read_csv('trend_analysis.csv')

# Convert the 'date' column to a datetime data type
df['date'] = pd.to_datetime(df['date'])

print(df.head())

# Set the 'date' column as the index of the DataFrame
df.set_index('date', inplace=True)

# Resample the data by day and count the number of entries in each day
# argument 'D' indicating that we want to resample by day.
# daily_counts = df.resample('D').count()
daily_counts = df.resample('D').count()
print("Daily Counts: \n", daily_counts)


# Plot the daily counts over time
plt.plot(daily_counts.index, daily_counts['id'])
plt.xlabel('Day')
plt.ylabel('Number of Entries')
plt.title('Social Media Trends')
plt.show()
