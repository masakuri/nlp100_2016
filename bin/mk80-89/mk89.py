# coding=utf-8

"""
89. 加法構成性によるアナロジー
85で得た単語の意味ベクトルを読み込み，vec("Spain") - vec("Madrid") + vec("Athens")を計算し，そのベクトルと類似度の高い10語とその類似度を出力せよ．
"""

import sys
from sklearn.externals import joblib
from scipy.spatial.distance import cosine
import cPickle as pickle
import numpy as np

word1 = sys.argv[1]
word2 = sys.argv[2]
word3 = sys.argv[3]
word_vectors = joblib.load("word_vectors.dump")
word_dic = pickle.load(sys.stdin)
word1 = word1.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_")
word2 = word2.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_")
word3 = word3.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_")

v1 = word_vectors[word_dic[word1]]
v2 = word_vectors[word_dic[word2]]
v3 = word_vectors[word_dic[word3]]

v = v1 - v2 + v3
cos_sim_top10 = list()
for word, idx in word_dic.iteritems():
    vc = word_vectors[idx]
    cos_sim = np.dot(v, vc) / (np.linalg.norm(v) * np.linalg.norm(vc))    # コサイン類似度計算
    if len(cos_sim_top10) < 10:   # 最初の10個は何も考えずにぶち込む
        cos_sim_top10.append((word, cos_sim))
        cos_sim_top10 = sorted(cos_sim_top10, key = lambda x: x[1], reverse=True) # コサイン類似度の高い順にソート
    else:
        if cos_sim > cos_sim_top10[9][1]:  # 現状の10位のコサイン類似度より今計算したコサイン類似度の方が大きかったら
            cos_sim_top10 = cos_sim_top10[0:9] + [(word, cos_sim)]   # 現状の10位を切り捨ててぶち込む
            cos_sim_top10 = sorted(cos_sim_top10, key=lambda x: x[1], reverse=True)  # コサイン類似度の高い順にソート

for word, cos_sim in cos_sim_top10:
    print "{} : {}".format(word, cos_sim)

"""
$ time python mk89.py "Spain" "Madrid" "Athens" < word_dic.pkl
Spain : 0.91053524173
Britain : 0.834713083249
Italy : 0.822808555325
Russia : 0.797953058852
Philadelphia : 0.796133878008
Scotland : 0.793301192083
Sweden : 0.790557778813
camp : 0.785923822673
both : 0.783548456442
New_Zealand : 0.778622245078
python mk89.py "Spain" "Madrid" "Athens" < word_dic.pkl  1.00s user 2.01s system 63% cpu 4.764 total
メモリ：400Mくらい？
"""
# うまくいってない

"""
$ python mk89.py "King" "man" "woman" < word_dic.pkl
King : 0.868296059242
woman : 0.838840377542
John : 0.82329138478
Lord : 0.806632424791
son : 0.806389415482
George : 0.802174287705
Henry : 0.799067156864
Prince : 0.795311373296
David : 0.794293994691
William : 0.793732857408
"""
# うーん
