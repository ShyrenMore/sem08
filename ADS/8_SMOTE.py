# from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
import seaborn as sns
from imblearn.over_sampling import SMOTE
df = pd.read_csv('Churn_Modelling.csv')
# df.head()

data = df[['CreditScore', 'Age', 'Exited']]
sns.scatterplot(data=data, x='CreditScore', y='Age', hue='Exited')

class_counts = data['Exited'].value_counts()
print(class_counts)

'''
0    7963
1    2037
Name: Exited, dtype: int64
'''

sns.countplot(x='Exited', data=data)
plt.title('Class Distribution')
plt.xlabel('Class Label')
plt.ylabel('Number of Examples')
plt.show()

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
#Splitting the data with stratification
X_train, X_test, y_train, y_test = train_test_split(data[['CreditScore', 'Age']], df['Exited'], test_size = 0.2, stratify = df['Exited'], random_state = 101)


# Without using SMOTE
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

print(classification_report(y_test, classifier.predict(X_test)))

smote = SMOTE(random_state = 101)
X_oversample, y_oversample = smote.fit_resample(X_train, y_train)
# Using SMOTE
classifier2 = LogisticRegression()
classifier2.fit(X_oversample, y_oversample)
print(classification_report(y_test, classifier2.predict(X_test)))
