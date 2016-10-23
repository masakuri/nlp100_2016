# coding=utf-8

"""
94. WordSimilarity-353での類似度計算
The WordSimilarity-353 Test Collectionの評価データを入力とし，1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を追加するプログラムを作成せよ．このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
"""

import sys
from sklearn.externals import joblib
import cPickle as pickle
import numpy as np

with open(sys.argv[1]) as WordSimilarity_353:
    word_vectors = joblib.load(sys.argv[2])
    word_dic = pickle.load(sys.stdin)
    for line in WordSimilarity_353.read().split("\n")[1:]:
        elem_ls = line.split()
        w1 = elem_ls[0]
        w2 = elem_ls[1]
        if word_dic.has_key(w1) and word_dic.has_key(w2):
            v1 = word_vectors[word_dic[w1]]
            v2 = word_vectors[word_dic[w2]]
            cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
            print "{}\t{}".format(line.rstrip("\r"), cos_sim)   # "^M"とかいうやつを削除するため「.rstrip("\r")」

"""
$ python mk94.py "set1.tab" "../mk80-89/word_vectors.dump" < ../mk80-89/word_dic.pkl > set1_85.tab
$ less set1_85.tab
love    sex 6.77    9   6   8   8   7   8   8   4   7   2   6   7   8   0.887544211834
tiger   cat 7.35    9   7   8   7   8   9   8.5 5   6   9   7   5   7   0.790014912109
tiger   tiger   10.00   10  10  10  10  10  10  10  10  10  10  10  10  10  1.0
...
$ python mk94.py "../../data/wordsim353/set1.tab" "word_vectors10.dump" < word_dic10.pkl > set1_90.tab
$ less set1_90.tab
love    sex 6.77    9   6   8   8   7   8   8   4   7   2   6   7   8   0.319856142143
tiger   cat 7.35    9   7   8   7   8   9   8.5 5   6   9   7   5   7   0.495095944286
tiger   tiger   10.00   10  10  10  10  10  10  10  10  10  10  10  10  10  1.0
...
"""
