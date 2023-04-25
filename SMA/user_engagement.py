# Exp 6
'''
To analyze how users engage with content on Twitter and understand what types of content are most engaging, we will use the following libraries:

pandas: for reading and manipulating the dataset
seaborn and matplotlib: for data visualization
nltk: for text processing
textblob: for sentiment analysis
wordcloud: for creating a word cloud of the most common words in the dataset
Assuming that the dataset is in a CSV format with a "text" column containing the tweet text, a "retweets" column containing the number of retweets, a "favorites" column containing the number of favorites, and a "date" column containing the date and time of the tweet, the program can be written as follows:
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
from wordcloud import WordCloud

# Read the dataset into a pandas DataFrame
df = pd.read_csv("engagement.csv")

# Remove stop words from the tweet text
# stop_words = set(stopwords.words("english"))
# df["text"] = df["text"].apply(lambda x: " ".join(
    # word for word in x.split() if word.lower() not in stop_words))

# Perform sentiment analysis using TextBlob and store the polarity score
df["polarity"] = df["text"].apply(lambda x: TextBlob(x).sentiment.polarity)

# Create a scatter plot of retweets vs. favorites to see how users engage with the content
sns.scatterplot(x="retweets", y="favorites", data=df)
plt.xlabel("Retweets")
plt.ylabel("Favorites")
plt.title("Engagement Analysis of Tweets")
plt.show()

# Create a bar chart of the most common words in the tweet text
wordcloud = WordCloud(background_color="white", max_words=50,
                      contour_width=3, contour_color="steelblue")
wordcloud.generate(" ".join(df["text"]))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Create a histogram of the polarity scores to see the distribution of sentiment in the dataset
sns.histplot(data=df, x=df["polarity"], bins=20)
plt.xlabel("Polarity Score")
plt.ylabel("Count")
plt.title("Sentiment Analysis of Tweets")
plt.show()
