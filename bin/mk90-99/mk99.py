# coding=utf-8

"""
99. t-SNEによる可視化
96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．
"""

import sys
import cPickle as pickle
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

country_vec_dic = pickle.load(sys.stdin)
country_names = country_vec_dic.keys()
country_vec = country_vec_dic.values()

tsne = TSNE(n_components=2)

country_vec_tsne = tsne.fit_transform(country_vec)
plt.scatter(country_vec_tsne[:, 0], country_vec_tsne[:, 1], s=0.01)
plt.title('t-SNE')
plt.xlabel('x')
plt.ylabel('y')
for country_name, vec in zip(country_names, country_vec_tsne):
    plt.annotate(country_name, xy = (vec[0], vec[1]), size = 3.)
plt.savefig("tsne.pdf")

"""
$ python mk99.py < country_vec_dic.pkl
http://www.cl.ecei.tohoku.ac.jp/~masakuri/nlp100/tsne.pdf
"""
