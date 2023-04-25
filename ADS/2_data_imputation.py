'''
#categorical to numerical 

from sklearn.preprocessing import OrdinalEncoder

data=df
oe =OrdinalEncoder()
result = oe.fit_transform(data)
print(result)
'''

import pandas as pd
df = pd.read_csv("london_weather.csv")
df.drop(['cloud_cover', 'global_radiation'], axis='columns')
print(df.head())

'''
Filling with means
means = df.mean()
# Fill in missing values with the column mean

df = df['cloud_cover'].fillna(df['cloud_cover'].means)
do same with median and mode and arbitratry values

df.ffill() i.e forwrad fill 
'''

import numpy as np
# random sample imputation
# curl -L -O https://github.com/ShyrenMore/sem08/archive/main.zip
df2 = df.copy()
missing = df2.isnull().sum()
print(missing)
for col in df2.columns:
    if(missing[col] > 0):
        values = df2[col].dropna().values
        # genereate random value from 1 to values?
        imputed_value = np.random.choice(values,size=missing[col])
        df2[col].loc[df2[col].isnull()] = imputed_value

print(df2.head())


# frequest category imputation
df3 = df.copy()
missing = df3.isnull().sum()
# Perform frequent category imputation for each column with missing values
for col in df3.columns:
    if missing[col] > 0:
        # Find the most frequent category in the column
        most_frequent = df3[col].mode()[0]
        df3[col].fillna(most_frequent, inplace=True)
df3.head()
