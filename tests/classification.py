# -*- coding: utf-8 -*-
import json
import os
import time

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

from preprocessings.ja.stopwords import get_stop_words
DATA_DIR = os.path.join(os.path.dirname(__file__), '../data/processed')


with open(os.path.join(DATA_DIR, 'livedoor_tokenized.json')) as f:
    livedoor = json.load(f)

start = time.time()
#stopwords = get_stop_words(livedoor['data'], n=100, min_freq=20)
livedoor['data'] = [' '.join(doc) for doc in livedoor['data']]
X_train, X_test, y_train, y_test = train_test_split(livedoor['data'], livedoor['label'], test_size=0.4)

parameters = {'n_estimators': [10, 30, 50, 70, 90, 110, 130, 150], 'max_features': ['auto', 'sqrt', 'log2', None]}
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', GridSearchCV(RandomForestClassifier(), parameters, cv=2, scoring='accuracy', verbose=10, n_jobs=-1)),
                     ])

text_clf = text_clf.fit(X_train, y_train)
print(text_clf.score(X_test, y_test))
y_pred = text_clf.predict(X_test)
print(classification_report(y_test, y_pred))
print('{}秒かかりました。'.format(time.time() - start))