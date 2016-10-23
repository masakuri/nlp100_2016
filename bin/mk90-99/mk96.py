# coding=utf-8

"""
96. 国名に関するベクトルの抽出
word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．
"""

import sys
from sklearn.externals import joblib
import cPickle as pickle

country_vec_dic = dict()
with open("../mk80-89/country_name.txt") as countries_name:
    word_vectors = joblib.load(sys.argv[1])
    word_dic = pickle.load(sys.stdin)
    for country_name in countries_name:
        country_name = country_name.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_")
        if word_dic.has_key(country_name.rstrip()):
            country_vec_dic[country_name] = word_vectors[word_dic[country_name.rstrip()]]
    pickle.dump(country_vec_dic, open("country_vec_dic.pkl", "w"))

"""
$ python mk96.py "word_vectors10.dump" < word_dic10.pkl
"""
