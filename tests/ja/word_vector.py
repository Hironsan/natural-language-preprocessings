import os
from unittest import TestCase

import numpy as np

from preprocessings.ja.word_vector import WordEmbeddings


class TestWordEmbeddings(TestCase):

    def setUp(self):
        self.word_embeddings = WordEmbeddings()
        self.save_path = 'model.bin'
        sentences = [
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'Ut rutrum diam sed sem dapibus feugiat. Nam suscipit nibh quis posuere accumsan.',
            'Quisque sed rutrum justo.',
            'Maecenas sit amet commodo eros. Morbi lectus erat, cursus vel tincidunt quis, luctus vitae nisi.',
            'Nunc risus tellus, interdum at nibh non, auctor placerat tortor.',
            'Aenean tristique nisi tempus, consequat lacus consectetur, vehicula orci.',
            'Morbi at vehicula ipsum. Etiam laoreet placerat odio quis volutpat.',
            'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.',
            'Etiam tempor sit amet nibh id sodales.',
            'Sed consectetur, mi vel laoreet lobortis, odio risus interdum augue, vitae finibus nulla dui placerat nulla.',
            'Praesent massa turpis, rhoncus in egestas non, egestas aliquet libero.',
            'Proin tincidunt magna sed ultricies ornare.',
            'Nullam tincidunt nisi id sagittis vehicula.',
        ]
        self.sentences = [sent.lower().split() for sent in sentences]

    def _remove_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)

    def test_train_word_embeddings(self):
        self.word_embeddings.train_word_embeddings(sentences=self.sentences, save_path=self.save_path, min_count=1)
        self.assertTrue(os.path.exists(self.save_path))
        self._remove_file(self.save_path)

    def test_load_word_embeddings(self):
        self.word_embeddings.train_word_embeddings(sentences=self.sentences, save_path=self.save_path, min_count=1)
        self.word_embeddings = WordEmbeddings()
        self.word_embeddings.load_word_embeddings(path=self.save_path)
        self.assertNotEqual(self.word_embeddings._model, None)
        self._remove_file(self.save_path)

    def test_get_word_vector(self):
        self.word_embeddings.train_word_embeddings(sentences=self.sentences, save_path=self.save_path, min_count=1)
        vector = self.word_embeddings.get_word_vector(term='lorem')
        self.assertEqual(vector.shape[0], 100)  # 100 dimension
        self.assertIsInstance(vector, np.ndarray)
        self.assertRaises(KeyError, self.word_embeddings.get_word_vector, term='Neko')
        self._remove_file(self.save_path)
