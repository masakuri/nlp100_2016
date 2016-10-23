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
word_vectors = joblib.load(sys.argv[4])
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
$ time python mk89.py "Spain" "Madrid" "Athens" "word_vectors.dump" < word_dic.pkl
Spain : 0.910455679946
Britain : 0.834547429776
Italy : 0.822756249557
Philadelphia : 0.800310605908
Russia : 0.799624596453
Scotland : 0.794285085503
Sweden : 0.790721696227
camp : 0.786801412759
both : 0.784217302251
collected : 0.778772531185
python mk89.py "Spain" "Madrid" "Athens" < word_dic.pkl  1.00s user 2.01s system 63% cpu 4.764 total
メモリ：400Mくらい？
"""
# うまくいってない

"""
$ python mk89.py "King" "man" "woman" "word_vectors.dump" < word_dic.pkl
King : 0.869005629632
woman : 0.837241396459
John : 0.821484842444
Lord : 0.806529645753
George : 0.806376869755
son : 0.806242872417
Henry : 0.796897808904
David : 0.794703102979
Prince : 0.793249795106
Richard : 0.792252611439
"""
# うーん

"""
Egypt : 0.854164597123
Spain : 0.851157174959
Poland : 0.845474717474
Greece : 0.840700558058
Britain : 0.835651541179
Hungary : 0.834935574771
Iran : 0.832932783031
Empire : 0.831729742483
Turkey : 0.824682832914
territory : 0.824372122845
python mk89.py "Spain" "Madrid" "Athens" "word_vectors10.dump" < word_dic.pkl  2.47s user 1.66s system 90% cpu 4.564 total（martini01）

King : 0.907485088296
woman : 0.889627480233
Prince : 0.888407006952
king : 0.885732169892
Princess : 0.882052644229
Queen : 0.880585729926
Elizabeth : 0.878119091327
Henry : 0.877643309423
sister : 0.876408515495
Lady : 0.87596697646（martini01）
"""
# 1/10
