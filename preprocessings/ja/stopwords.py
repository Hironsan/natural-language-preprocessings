# -*- coding: utf-8 -*-
import os
import urllib.request
from collections import Counter

from gensim import corpora


def maybe_download(path):
    url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
    if os.path.exists(path):
        print('File already exists.')
    else:
        print('Downloading...')
        # Download the file from `url` and save it locally under `file_name`:
        urllib.request.urlretrieve(url, path)


def create_dictionary(texts):
    dictionary = corpora.Dictionary(texts)
    return dictionary


def remove_stopwords(words, stopwords):
    words = [word for word in words if word not in stopwords]
    return words


def most_common(text, n=100):
    fdist = Counter()
    for word in text:
        fdist[word] += 1
    common_words = {word for word, freq in fdist.most_common(n)}
    return common_words