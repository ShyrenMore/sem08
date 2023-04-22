import pandas as pd
import numpy as np

df = pd.read_csv("london_weather.csv")
# print(df.head())

df = df[['cloud_cover', 'sunshine', 'global_radiation',
         'max_temp', 'min_temp', 'precipitation']]
# print(df.describe())
# print(df.info())
# print(df.corr())
# print(df.count())

# print(df.median())
# print(df.mode())
# print(df.skew())
# print(df.kurtosis())
# print(df.var())
# print(df.sem())

import matplotlib.pyplot as plt
plt.scatter(df['cloud_cover'], df['sunshine'], c='blue')
# plt.show()
# do the same for all the params i.e change X

print('-No. of missing values-')
print(df.isnull().sum())

# boxplot
box_df = df[['min_temp', 'max_temp']]
fig = plt.figure(figsize=(10, 7))
plt.boxplot(box_df.head(50))
plt.show()

# Trimmed mean of 10%
from scipy import stats
print(stats.trim_mean(df['cloud_cover'], 0.1))