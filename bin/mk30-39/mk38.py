# coding=utf-8

"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""

import numpy as np
import matplotlib.pyplot as plt
import mk36
from collections import defaultdict

data = mk36.word_count()
i = 0
xlabel = []
ylabel = []
value_counter = defaultdict(int)
for value in data.values():
    value_counter[value] += 1
for k, v in sorted(value_counter.iteritems(), key = lambda x: x[0]):
    xlabel.append(k)
    ylabel.append(v)

plt.bar(xlabel, ylabel, align = "center")
plt.xlim(0, 20)
plt.show()

"""
http://www.cl.ecei.tohoku.ac.jp/~masakuri/nlp100/mk38.html
"""
