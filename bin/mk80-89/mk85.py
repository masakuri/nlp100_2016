# coding=utf-8

"""
85. 主成分分析による次元圧縮
84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．
"""

import sys
import cPickle as pickle
from sklearn.externals import joblib
import sklearn.decomposition as decomp

tc_matrix = joblib.load(sys.argv[1])
# pca = decomp.PCA(n_components=300) # これでしようとすると zsh: killed される．．．
# word_vectors = pca.fit_transform(tc_matrix.toarray())
svd = decomp.TruncatedSVD(300)
word_vectors = svd.fit_transform(tc_matrix)
joblib.dump(word_vectors, "word_vectors.dump")

"""
$ time python mk85.py wc_array.pkl
python mk85.py wc_array.pkl  177.23s user 64.31s system 102% cpu 3:55.54 total
メモリ：1.4Gくらい
"""
