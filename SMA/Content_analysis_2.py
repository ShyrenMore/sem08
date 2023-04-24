'''
This program first loads the social media data from a CSV file and removes any rows with missing values. It then uses the langdetect library to remove any non-English content, and performs text preprocessing by removing stopwords and performing lemmatization using the NLTK library.

Next, it creates a document-term matrix using TF-IDF vectorization, and converts it to a gensim corpus. It then uses the LdaModel class from gensim to perform LDA topic modeling on the corpus, specifying the number of topics to be 5.

Finally, it visualizes the topics using the pyLDAvis library, which generates an interactive visualization of the topics. You can then use this visualization to explore the topics and their associated words and documents.

'''

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import csv
import numpy as np
import pandas as pd
from langdetect import detect
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim import corpora, models
import pyLDAvis.gensim

# Load social media data from a CSV file
data = pd.read_csv("social_media_data.csv")

# Remove any rows with missing values
data = data.dropna()

# Remove any non-English content
data['language'] = data['text'].apply(lambda x: detect(x))
data = data[data['language'] == 'en']

# Clean up the text by removing stopwords and performing lemmatization
stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()


def preprocess(text):
    words = TextBlob(text).words.singularize()
    words = [lemmatizer.lemmatize(word)
             for word in words if word not in stop_words]
    return ' '.join(words)


data['clean_text'] = data['text'].apply(preprocess)

# Create a document-term matrix using TF-IDF vectorization
vectorizer = TfidfVectorizer()
doc_term_matrix = vectorizer.fit_transform(data['clean_text'])

# Convert the document-term matrix to a gensim corpus
corpus = corpora.MmCorpus(doc_term_matrix.transpose())

# Perform LDA topic modeling on the corpus
lda_model = models.LdaModel(
    corpus=corpus, num_topics=5, id2word=vectorizer.get_feature_names())

# Visualize the topics using pyLDAvis
pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim.prepare(lda_model, corpus, vectorizer)
pyLDAvis.display(vis)

'''
The output of the above code would be an interactive visualization of the topics generated by the LDA model using the pyLDAvis library. The visualization would show the following:

A two-dimensional plot of the topics, where each circle represents a topic and the size of the circle represents the prevalence of the topic in the corpus.
A list of the top 30 most relevant terms for each topic, where relevance is calculated as a combination of the term frequency and the exclusivity of the term to the topic.
A horizontal bar chart that shows the frequency of each term in the corpus, along with its overall frequency across all topics.
'''