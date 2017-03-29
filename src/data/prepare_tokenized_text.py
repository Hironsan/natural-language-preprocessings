# -*- coding: utf-8 -*-
import json
import os

import tqdm

from preprocessings.ja.tokenizer import MeCabTokenizer
DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data/processed')


if __name__ == '__main__':
    with open(os.path.join(DATA_DIR, 'livedoor.json')) as f:
        livedoor = json.load(f)

    tokenizer = MeCabTokenizer()

    data = []
    for doc in tqdm.tqdm(livedoor['data']):
        new_doc = '\n'.join(sent.strip() for sent in doc.split('\n')[2:] if sent != '')  # skip header by [2:]
        words = tokenizer.wakati_baseform(new_doc)
        data.append(words)
    livedoor['data'] = data

    # livedoor['data'] = [tokenizer.wakati_baseform(sent) for sent in tqdm.tqdm(livedoor['data'])]
    with open(os.path.join(DATA_DIR, 'livedoor_tokenized.json'), 'w') as f:
        json.dump(livedoor, f)
