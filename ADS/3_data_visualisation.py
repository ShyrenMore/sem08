import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("london_weather.csv")

# print(df.describe())
# print(df.info())
# print(df.corr())
# print(df.count())

plt.scatter(df['cloud_cover'], df['sunshine'], c='blue')
# plt.show()

g = sns.displot(df['min_temp']) # distri plot

# Draw a plot of two variables with bivariate and univariate graphs: jointplot
sns.jointplot(x = 'min_temp', y='max_temp', data=df)

# Plot pairwise relationships in a dataset: pairplot
sns.pairplot(df)
plt.show()


# Plot marginal distributions by drawing ticks along the x and y axes: rugplot
plt.figure(figsize=(15, 5))
sns.scatterplot(data=df.head(20), x="min_temp")
sns.rugplot(data=df.head(20), x='min_temp')
plt.show()

# Histogram
# Histogram
df['min_temp'].hist()
plt.show()

'''
Andrew's curve
'''
df1 = df[['min_temp', 'cloud_cover', 'max_temp']]
df1 = df1.sample(n=50)
andrew = pd.plotting.andrews_curves(df1, 'min_temp')
andrew.plot()
plt.show()
