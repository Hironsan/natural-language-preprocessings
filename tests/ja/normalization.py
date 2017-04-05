# -*- coding: utf-8 -*-
from unittest import TestCase
from preprocessings.ja.normalization import normalize_unicode, lower_text, normalize_number


class TestNormalizeUnicode(TestCase):

    def test_normalize_unicode(self):
        text = 'ＢＣＤ'  # 全角アルファベット
        normalized_text = normalize_unicode(text)
        self.assertEqual(normalized_text, 'BCD')
        text = 'ｂｃｄ'  # 全角アルファベット
        normalized_text = normalize_unicode(text)
        self.assertEqual(normalized_text, 'bcd')
        text = 'CAT'  # 半角アルファベット
        normalized_text = normalize_unicode(text)
        self.assertEqual(normalized_text, 'CAT')
        text = 'cat'  # 半角アルファベット
        normalized_text = normalize_unicode(text)
        self.assertEqual(normalized_text, 'cat')
        text = 'ネコ'
        normalized_text = normalize_unicode(text)
        self.assertEqual(normalized_text, 'ネコ')
        text = 'ねこ'
        normalized_text = normalize_unicode(text)
        self.assertEqual(normalized_text, 'ねこ')
        text = '猫'
        normalized_text = normalize_unicode(text)
        self.assertEqual(normalized_text, '猫')
        text = 'ﾈｺ'
        normalized_text = normalize_unicode(text)
        self.assertEqual(normalized_text, 'ネコ')
        text = '　'  # 全角スペース
        normalized_text = normalize_unicode(text)
        self.assertEqual(normalized_text, ' ')
        text = '＠'  # 全角アットマーク
        normalized_text = normalize_unicode(text)
        self.assertEqual(normalized_text, '@')

    def test_lower_text(self):
        text = 'ABc'
        normalized_text = lower_text(text)
        self.assertEqual(normalized_text, 'abc')

    def test_replace_numbers_by_zero(self):
        text = '2009年4月6日'
        result = normalize_number(text)
        self.assertEqual(result, '0年0月0日')
