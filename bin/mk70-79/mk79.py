# coding=utf-8

"""
79. 適合率-再現率グラフの描画
ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ．
"""

import sys
import matplotlib.pyplot as plt
import numpy as np

result_data = sys.stdin
positive = list()
negative = list()
precision_list = list()
recall_list = list()

for line in result_data:
    answer, predict, prob = line.rstrip().split("\t")
    if answer == "+1":
        positive.append(float(prob))
    elif answer == "-1":
        negative.append(float(prob))

positive_array = np.array(positive)
negative_array = np.array(negative)

for p in np.arange(0.05, 1.0, 0.05):
    true_positive = len(positive_array[positive_array >= p])
    true_negative = len(negative_array[negative_array < p])
    false_positive = len(negative_array[negative_array >= p])
    false_negative = len(positive_array[positive_array < p])

    precision_list.append(float(true_positive) / float(true_positive + false_positive))
    recall_list.append(float(true_positive) / float(true_positive + false_negative))

plt.xlim(0.0, 1.1)
plt.ylim(0.0, 1.1)
plt.plot(precision_list, recall_list)
plt.legend()
plt.grid()
plt.xlabel("precision")
plt.ylabel("recall")
plt.show()

"""
$ python mk79.py < result_base.txt
http://www.cl.ecei.tohoku.ac.jp/~masakuri/nlp100/base.png
$ python mk79.py < result_all.txt
http://www.cl.ecei.tohoku.ac.jp/~masakuri/nlp100/all.png
"""
