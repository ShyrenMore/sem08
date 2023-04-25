from sklearn.preprocessing import MinMaxScaler
import pandas as pd
df = pd.read_csv("london_weather.csv")

df.drop(['date'], axis='columns', inplace=True)
sunshine_median = df['sunshine'].median()
df = df.fillna(df.median())

transform = lambda x: 1 if x >= sunshine_median else 0
df['sunshine'] = df['sunshine'].apply(transform)

X = df.drop('sunshine', axis='columns')
y = df.sunshine

scaler = MinMaxScaler()
X_sc = scaler.fit_transform(X)
print(X_sc)     # numpy array
df_scaled = pd.DataFrame(X_sc, columns=X.columns)
print(df_scaled.head())

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

cor = X.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(cor, annot=True)
plt.show()

kmeans = KMeans(n_clusters=2)
kmeans.fit(X_sc)
y_pred = kmeans.fit_predict(X_sc)

labels = kmeans.labels_
# centroids = kmeans.cluster_centers_

# Extrinsince metrics: Rand index, Rand score, Mutual info
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score, rand_score, silhouette_score
print(adjusted_rand_score(y, y_pred)) # rand index
print(rand_score(y, y_pred)) # rand score
print(normalized_mutual_info_score(y, y_pred)) #mutual info

# Intrinsic metrics: Silhouette Coefficient
# from sklearn.metrics import silhouette_score
print(silhouette_score(X, labels))
