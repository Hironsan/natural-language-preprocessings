# -*- coding: utf-8 -*-
import json
import os
import tarfile
import urllib.request
from collections import defaultdict
DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data')


def download_corpus(url, save_path):
    file_name = url.split('/')[-1]
    file_name = os.path.join(save_path, file_name)
    if os.path.exists(file_name):
        print('{} already exists.'.format(file_name))
    else:
        print('Downloading {}'.format(file_name))
        file_name, _ = urllib.request.urlretrieve(url, file_name)
    return file_name


def extract_file(file_name, path):
    with tarfile.open(file_name, "r:gz") as tar:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, path)


def load_corpus(path):
    corpus = {'data': [], 'label': [], 'label_names': []}
    vocabulary = defaultdict()
    vocabulary.default_factory = vocabulary.__len__
    for file_or_dir in os.listdir(path):
        if file_or_dir.endswith('.txt'):
            continue
        label = file_or_dir
        for file in os.listdir(os.path.join(path, label)):
            if file == 'LICENSE.txt':
                continue
            with open(os.path.join(path, label, file)) as f:
                text = f.read()
                corpus['data'].append(text)
                corpus['label'].append(vocabulary[label])
    corpus['label_names'] = dict((v, k) for k, v in vocabulary.items())
    return corpus


def save_data(data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data, f)


def main(raw_dir, processed_dir):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    url = 'http://www.rondhuit.com/download/ldcc-20140209.tar.gz'
    file_name = download_corpus(url=url, save_path=raw_dir)
    extract_file(file_name, raw_dir)
    raw_data = load_corpus(os.path.join(raw_dir, 'text'))
    save_data(raw_data, os.path.join(processed_dir, 'livedoor.json'))


if __name__ == '__main__':
    # not used in this stub but often useful for finding various files
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    raw_dir = os.path.join(project_dir, 'data/raw')
    processed_dir = os.path.join(project_dir, 'data/processed')

    main(raw_dir, processed_dir)
