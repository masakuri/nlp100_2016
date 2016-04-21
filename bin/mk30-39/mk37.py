# coding=utf-8

"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

import numpy as np
import matplotlib.pyplot as plt
import mk36

data = mk36.word_count()
i = 0
xlabel = []
ylabel = []
plt.rcParams['font.family'] = u'TakaoPGothic'
for word, freq in sorted(data.iteritems(), key = lambda x: x[1], reverse = True):
    if i < 10:
        xlabel.append(word.decode("utf-8"))
        ylabel.append(freq)
        i += 1
    else:
        break

x = range(10)
plt.bar(x, ylabel, align = "center")
plt.xticks(x, xlabel)
plt.show()

"""
http://www.cl.ecei.tohoku.ac.jp/~masakuri/nlp100/mk37.html
"""
