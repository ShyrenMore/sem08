import pandas as pd

# !pip install pyLDAvis
import pyLDAvis.gensim_models

from gensim import corpora
from gensim.models import LdaModel
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

df = pd.read_csv('social_media_data.csv')

stop_words = set(STOPWORDS)
def preprocess(text):
    result = []
    for token in simple_preprocess(text):
        if token not in stop_words:
            result.append(token)

    return result


texts = df['text'].apply(preprocess)
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

num_topics = 5
passes = 10
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, passes=passes)

for topic in lda_model.print_topics():
    print(topic)

vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
pyLDAvis.display(vis)

