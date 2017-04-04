# -*- coding:utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


corpus = [
	'This is a pen.',
	'That is a bot.',
	'These are red document and blue document.',
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X.toarray())

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X.toarray())
