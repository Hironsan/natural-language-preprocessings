# -*- coding: utf-8 -*-
import json
import unittest

from preprocessings.ja.cleaning import clean_html_tags, clean_html_and_js_tags, clean_code, clean_url


class TestCleaning(unittest.TestCase):

    def setUp(self):
        self.html_text = open('data/test.html').read()

    def test_clean_html_tag(self):
        clean_text = clean_html_tags(self.html_text)
        self.assertTrue('<span color="red">' not in clean_text)
        print(clean_text)

    def test_clean_javascript_tag(self):
        clean_text = clean_html_and_js_tags(self.html_text)
        self.assertTrue('<span color="red">' not in clean_text)
        self.assertTrue('var textbook' not in clean_text)
        print(clean_text)

    def test_qiita_text(self):
        with open('data/qiita.json') as f:
            qiita_json = json.load(f)
        html_text = qiita_json['rendered_body']
        clean_text = clean_code(html_text)
        print(clean_text)

    def test_clean_url(self):
        with open('data/qiita.json') as f:
            qiita_json = json.load(f)
        html_text = qiita_json['rendered_body']
        clean_text = clean_code(html_text)
        clean_text = clean_url(clean_text)
        print(clean_text)
