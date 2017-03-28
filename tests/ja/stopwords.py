# -*- coding: utf-8 -*-
import os
import unittest

from preprocessings.ja.stopwords import maybe_download, create_dictionary, most_common
from preprocessings.ja.tokenizer import JanomeTokenizer


class TestStopwords(unittest.TestCase):

    def setUp(self):
        self.filename = 'stop-words.ja.txt'
        self._remove_file()

    def tearDown(self):
        self._remove_file()

    def _remove_file(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_download(self):
        self.assertFalse(os.path.exists(self.filename))
        maybe_download(self.filename)
        self.assertTrue(os.path.exists(self.filename))

    def test_read_stopwords(self):
        maybe_download(self.filename)
        stopwords = {line.strip() for line in open(self.filename) if line != '\n'}
        self.assertTrue(len(stopwords) > 0)


class TestDictionary(unittest.TestCase):

    def setUp(self):
        document = open('data/document.txt').read()
        self.text = self._tokenize(document)

    def _tokenize(self, sent):
        tokenizer = JanomeTokenizer()
        words = tokenizer.wakati(sent.lower())
        return words

    def test_most_common(self):
        words = most_common(self.text, n=10)
        print(words)

    def test_create_dictionary(self):
        dictionary = create_dictionary(self.text)
        dictionary.filter_n_most_frequent(remove_n=10)
        print(dictionary.token2id)
        dictionary.filter_extremes(no_below=2, no_above=0.9)
        print(dictionary.token2id)