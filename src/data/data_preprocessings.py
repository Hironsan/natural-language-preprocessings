# -*- coding: utf-8 -*-
import json
import os

from joblib import Parallel, delayed

from preprocessings.ja.tokenizer import MeCabTokenizer
from preprocessings.ja.normalization import normalize
from preprocessings.ja.cleaning import clean_text
DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data/processed')


def process(text):
    text = clean_text(text)
    words = tokenizer.wakati_baseform(text)
    words = [normalize(word) for word in words]
    return words


if __name__ == '__main__':
    with open(os.path.join(DATA_DIR, 'livedoor.json')) as f:
        livedoor = json.load(f)

    tokenizer = MeCabTokenizer('/usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
    data = Parallel(n_jobs=-1)([delayed(process)(text) for text in livedoor['data']])
    livedoor['data'] = data

    with open(os.path.join(DATA_DIR, 'livedoor_tokenized_neologd.json'), 'w') as f:
        json.dump(livedoor, f)
