import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

df = load_iris()
print(df)
X = df.data
y = df.target


from sklearn.neighbors import NearestNeighbors
model = NearestNeighbors(n_neighbors=3)
model.fit(X, y)

# distances and indexes of k-neaighbors from model outputs
distances, indexes = model.kneighbors(X)
# plot mean of k-distances of each observation
plt.plot(distances.mean(axis=1))
plt.show()

# print("\nType os :: \n", type(distances))
# cut outlier values of >0.15 
outlier_idx = np.where(distances.mean(axis=1) > 0.15)
# filter outlier values
outlier_attributes = df.data[outlier_idx]
print(outlier_attributes)
