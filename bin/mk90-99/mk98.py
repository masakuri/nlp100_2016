# coding=utf-8

"""
98. Ward法によるクラスタリング
96の単語ベクトルに対して，Ward法による階層型クラスタリングを実行せよ．さらに，クラスタリング結果をデンドログラムとして可視化せよ．
"""

import sys
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
import cPickle as pickle

country_vec_dic = pickle.load(sys.stdin)
country_names = country_vec_dic.keys()
country_vec = country_vec_dic.values()
ward = linkage(country_vec, method="ward")
dendrogram(ward, leaf_font_size=1.5, orientation='left', labels=[country for country in country_names])
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('distance')
plt.ylabel('country')
plt.savefig("dendrogram.pdf")

"""
$ python mk98.py < country_vec_dic.pkl
http://www.cl.ecei.tohoku.ac.jp/~masakuri/nlp100/dendrogram.pdf
"""
