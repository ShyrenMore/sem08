# Exp 5
'''
This program first reads the dataset into a pandas DataFrame. Then, it uses TextBlob to perform sentiment analysis on each tweet and stores the polarity score in a new column called "polarity".

Next, it creates separate DataFrames for positive and negative tweets using the "label" column. Finally, it plots the distribution of polarity scores for positive and negative tweets using seaborn and matplotlib. The resulting plot shows the density of polarity scores for each sentiment label, allowing us to compare the distribution of sentiment in the dataset.

Note that this is a very basic example of sentiment analysis and there are many ways to improve it, such as using more advanced natural language processing techniques, handling negation and sarcasm, and using a larger and more diverse dataset.
'''

import pandas as pd
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset into a pandas DataFrame
df = pd.read_csv("sentiment.csv")

# Perform sentiment analysis using TextBlob and store the polarity score
df["polarity"] = df["text"].apply(lambda x: TextBlob(x).sentiment.polarity)
print(df.head())

# Create separate DataFrames for positive and negative tweets
pos_tweets = df[df["label"] == "positive"]
neg_tweets = df[df["label"] == "negative"]

# Plot the distribution of polarity scores for positive and negative tweets
# A kernel density estimate (KDE) plot is a method for visualizing the distribution of observations in a dataset, analogous to a histogram.
sns.kdeplot(pos_tweets["polarity"], shade=True, label="Positive")
sns.kdeplot(neg_tweets["polarity"], shade=True, label="Negative")
plt.xlabel("Polarity Score")
plt.ylabel("Density")
plt.title("Sentiment Analysis of Tweets")
plt.legend()
plt.show()
