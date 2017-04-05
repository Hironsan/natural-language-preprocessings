# -*- coding: utf-8 -*-
import json
import os

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

from preprocessings.ja.stopwords import most_common
DATA_DIR = os.path.join(os.path.dirname(__file__), '../data/processed')


with open(os.path.join(DATA_DIR, 'livedoor_tokenized_processed.json')) as f:
    livedoor = json.load(f)

stopwords = most_common(livedoor['data'])
livedoor['data'] = [' '.join(doc) for doc in livedoor['data']]
X_train, X_test, y_train, y_test = train_test_split(livedoor['data'], livedoor['label'], test_size=0.4)
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

parameters = {'n_estimators': [10, 30, 50, 70, 90, 110, 130, 150], 'max_features': ['auto', 'sqrt', 'log2', None]}


from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect', CountVectorizer(stop_words=stopwords, min_df=20)),
                     ('tfidf', TfidfTransformer()),
                     #('clf', MultinomialNB()),
                     ('clf', RandomForestClassifier()),
                     #('clf', GridSearchCV(RandomForestClassifier(), parameters, cv=2, scoring='accuracy', verbose=10, n_jobs=4)),
                     ])

text_clf = text_clf.fit(X_train, y_train)
print(text_clf.score(X_test, y_test))
print(dir(text_clf))
print(dir(text_clf.named_steps['clf']))
print(text_clf.named_steps['clf'].feature_importances_)
print(len(text_clf.named_steps['clf'].feature_importances_))
import numpy as np
print(np.argmax(text_clf.named_steps['clf'].feature_importances_))
y_pred = text_clf.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
