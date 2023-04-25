from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr
import pandas as pd
df = pd.read_csv("london_weather.csv")
df.head()

df = df.fillna(df.mean())
# print("After filling NUll values")
# print(df.head())

df.describe()

sunshine_median = df['sunshine'].median()
# In sunshine we want only 0/1
# currently it has a range of values 0 to some int
transform = lambda x: 1 if x>=sunshine_median else 0
# Apply the transformation to the "sunshine" column
df['sunshine'] = df['sunshine'].apply(transform)

X = df.drop(['sunshine', 'date'], axis='columns')
# normalize all cols
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_sc = scaler.fit_transform(X)
print(X_sc)     # numpy array
df_scaled = pd.DataFrame(X_sc, columns=X.columns)
print(df_scaled.head())

# classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
target = df['sunshine']

X_train, X_test, y_train, y_test = train_test_split(df_scaled, target, train_size=0.8)

model = KNeighborsClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_auc_score

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()   # flattened array
print("True Negatives {}".format(tn))
print("False Negatives {}".format(fn))
print("True Positives {}".format(tp))
print("False Positives {}".format(fp))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Error:", 1-accuracy_score(y_test, y_pred))
print("ROC area under the curve score:", roc_auc_score(y_test, y_pred))

specificity = tp/(tp+fn)
print("Specificity:", specificity)
print("False Positive Rate: ", 1-specificity)

# plotting ROC curve
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt 
fpr, tpr, thresholds = roc_curve(y_test, y_pred)
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()

# doing linear reg for Karl pearson, R^2, MSE, RMSE, MAE
X = df_scaled.min_temp
y = df_scaled.max_temp
# Karl pearson (has to be before re-shaping)
corr, _ = pearsonr(X, y)
print("Karl Pearson's coefficient of correlation:", corr)

# R-squared
reg = LinearRegression()
X = X.values
X = X.reshape(-1, 1)
reg.fit(X, y)
y_pred = reg.predict(X)
r_squared = r2_score(y, y_pred)
print("R-squared:", r_squared)

# MSE
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error:", mse)

import math

rmse = math.sqrt(mse)
print("RMSE:", rmse)


# MAE
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y, y_pred)
print("MAE:", mae)

print("MAPE:", mae*100, end="%")