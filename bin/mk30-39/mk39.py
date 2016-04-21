# coding=utf-8

"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

import numpy as np
import matplotlib.pyplot as plt
import mk36
from collections import defaultdict

data = mk36.word_count()
i = 1
j = 1
freq = []
cnt = []
xlabel = []
ylabel = []

# 38と同様に出現頻度と出現頻度をとる単語の種類数のリスト作成
value_counter = defaultdict(int)
for value in data.values():
    value_counter[value] += 1
for k, v in sorted(value_counter.iteritems(), key = lambda x: x[0], reverse = True):
    freq.append(k)
    cnt.append(v)

# 順位作成
for num in freq:
    xlabel.append(i)
    ylabel.append(num)
    i = i + cnt[j - 1]
    j += 1

# プロット
plt.xscale("log")
plt.yscale("log")
plt.plot(xlabel, ylabel, ".")
plt.show()

"""
http://www.cl.ecei.tohoku.ac.jp/~masakuri/nlp100/mk39.html
"""
