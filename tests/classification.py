# -*- coding: utf-8 -*-
import json
import os

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

from preprocessings.ja.tokenizer import MeCabTokenizer
DATA_DIR = os.path.join(os.path.dirname(__file__), '../data/processed')


with open(os.path.join(DATA_DIR, 'livedoor.json')) as f:
    livedoor = json.load(f)

tokenizer = MeCabTokenizer()
X_train, X_test, y_train, y_test = train_test_split(livedoor['data'], livedoor['label'], test_size=0.4, random_state=0)
"""
count_vect = CountVectorizer(analyzer=tokenizer.wakati_baseform)
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
from sklearn.naive_bayes import MultinomialNB
text_clf = MultinomialNB().fit(X_train_tfidf, y_train)
"""
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect', CountVectorizer(analyzer=tokenizer.wakati)),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),
                     ])

text_clf = text_clf.fit(X_train, y_train)
text_clf.score(X_test, y_test)
