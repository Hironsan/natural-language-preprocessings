# Natural Language Pre-processing
This repository includes some recipes of natural language pre-processing.

The list of recipes are as follows:
* Data cleaner
* Word normalization
* Stopwords remover
* Tokenizer
* Word Vector


## Install
To install required modules, simply:

```
$ pip install -r requirements.txt
```

## Setup
First, you should download [livedoor news corpus](http://www.rondhuit.com/download.html#ldcc) and extract it.
For downloading the corpus, please execute following command:

```
$ cd src/data
$ python make_dataset.py
```

Now, you can ready for classification!

Start jupyter notebook:

```
$ jupyter notebook
```

And you can execute [notebooks/document_classification.ipynb](https://github.com/Hironsan/natural-language-preprocessings/blob/master/notebooks/document_classification.ipynb).

Good NLP Life!

## Licence

[MIT](https://github.com/Hironsan/natural-language-preprocessings/blob/master/LICENCE)

## Author

[Hironsan](https://github.com/Hironsan)