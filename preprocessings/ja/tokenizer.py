# -*- coding: utf-8 -*-
from collections import namedtuple

import MeCab
from janome.tokenizer import Tokenizer


class JanomeTokenizer(object):

    def __init__(self, user_dic_path='', user_dic_enc='utf8'):
        self._t = Tokenizer(udic=user_dic_path, udic_enc=user_dic_enc)

    def wakati(self, sent):
        words = [token.surface for token in self.tokenize(sent)]
        return words

    def wakati_baseform(self, sent):
        words = [token.base_form if token.base_form != '*' else token.surface
                 for token in self.tokenize(sent)]
        return words

    def tokenize(self, sent):
        for t in self._t.tokenize(sent):
            token = namedtuple('Token', 'surface, pos, pos_detail1, pos_detail2, pos_detail3,\
                                                 infl_type, infl_form, base_form, reading, phonetic')
            poses = t.part_of_speech.split(',')
            token.surface = t.surface        # 表層形
            token.pos = poses[0]             # 品詞
            token.pos_detail1 = poses[1]     # 品詞細分類1
            token.pos_detail2 = poses[2]     # 品詞細分類2
            token.pos_detail3 = poses[3]     # 品詞細分類3
            token.infl_type = t.infl_type    # 活用型
            token.infl_form = t.infl_form    # 活用形
            token.base_form = t.base_form    # 原型
            token.reading = t.reading        # 読み
            token.phonetic = token.phonetic  # 発音
            yield token

    def filter_by_pos(self, sent, pos=('名詞', )):
        tokens = [token for token in self.tokenize(sent) if token.pos in pos]
        return tokens


class MeCabTokenizer(object):

    def __init__(self, user_dic_path='', sys_dic_path=''):
        option = '-Ochasen'
        if user_dic_path:
            option += ' -u {0}'.format(user_dic_path)
        if sys_dic_path:
            option += ' -u {0}'.format(sys_dic_path)
        self._t = MeCab.Tagger(option)

    def wakati(self, sent):
        words = [token.surface for token in self.tokenize(sent)]
        return words

    def wakati_baseform(self, sent):
        words = [token.base_form if token.base_form != '*' else token.surface
                 for token in self.tokenize(sent)]
        return words

    def tokenize(self, sent):
        self._t.parse('')  # for UnicodeDecodeError
        node = self._t.parseToNode(sent)

        while node:
            token = namedtuple('Token', 'surface, pos, pos_detail1, pos_detail2, pos_detail3,\
                                                     infl_type, infl_form, base_form, reading, phonetic')
            feature = node.feature.split(',')
            token.surface = node.surface    # 表層形
            token.pos = feature[0]          # 品詞
            token.pos_detail1 = feature[1]  # 品詞細分類1
            token.pos_detail2 = feature[2]  # 品詞細分類2
            token.pos_detail3 = feature[3]  # 品詞細分類3
            token.infl_type = feature[4]    # 活用型
            token.infl_form = feature[5]    # 活用形
            token.base_form = feature[6]    # 原型
            token.reading = feature[7] if len(feature) > 7 else ''    # 読み
            token.phonetic = feature[8] if len(feature) > 8 else ''   # 発音
            yield token
            node = node.next

    def filter_by_pos(self, sent, pos=('名詞',)):
        tokens = [token for token in self.tokenize(sent) if token.pos == pos]
        return tokens
