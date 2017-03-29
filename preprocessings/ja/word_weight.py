import json
import os
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.model_selection import train_test_split


file_name = os.path.join(os.path.dirname(__file__), '../../data/processed/livedoor_tokenized.json')
with open(file_name) as f:
    livedoor = json.load(f)

docs = livedoor['data']
docs = [' '.join(d) for d in docs]
X_train, X_test, y_train, y_test = train_test_split(docs, livedoor['label'], test_size=0.4, random_state=0)

#tfidf_transformer = TfidfTransformer()
#X_train_tfidf = tfidf_transformer.fit_transform(texts)
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(docs)
print(X_train.shape)
print(y_train.shape)
from sklearn.naive_bayes import MultinomialNB
text_clf = MultinomialNB().fit(X_train, y_train)
print(text_clf.score(X_test, y_test))

