# coding=utf-8

"""
95. WordSimilarity-353での評価
94で作ったデータを用い，各モデルが出力する類似度のランキングと，人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
"""

import sys
from scipy.stats import spearmanr

data = sys.stdin
human_sim = list()
model_sim = list()
for line in data:
    elem_list = line.rstrip().split("\t")
    human_sim.append(elem_list[2])
    model_sim.append(elem_list[-1])
print spearmanr(human_sim, model_sim)

"""
$ python mk95.py < set1_85.tab
SpearmanrResult(correlation=0.28117468482368646, pvalue=0.0004497901672237896)
$ python mk95.py < set1_90.tab
SpearmanrResult(correlation=0.64460368202756491, pvalue=2.4546202395053548e-19)
"""
