# coding=utf-8
"""
88. 類似度の高い単語10件
85で得た単語の意味ベクトルを読み込み，"England"とコサイン類似度が高い10語と，その類似度を出力せよ．
"""
import sys
from sklearn.externals import joblib
import cPickle as pickle
import numpy as np

target_word = sys.argv[1]
word_vectors = joblib.load(sys.argv[2])
word_dic = pickle.load(sys.stdin)
target_word = target_word.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_")
cos_sim_top10 = list()

v1 = word_vectors[word_dic[target_word]]

for word, idx in word_dic.iteritems():
    v2 = word_vectors[idx]
    cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))    # コサイン類似度計算
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
$ time python mk88.py "England" "word_vectors.dump" < word_dic.pkl
England : 1.0
France : 0.88950632473
Australia : 0.883783587441
Germany : 0.881372142281
London : 0.873201747638
India : 0.863680423084
West : 0.861870126889
home : 0.861744815153
America : 0.859038989959
Japan : 0.855082067514
python mk88.py "England" < word_dic.pkl  0.92s user 1.92s system 63% cpu 4.472 total
メモリ：300Mくらい？

$ python mk88.py "leader" "word_vectors.dump" < word_dic.pkl
leader : 1.0
president : 0.876436996247
governor : 0.874899102844
partner : 0.866409267281
manager : 0.860153406591
director : 0.853685538917
head : 0.850297840033
member : 0.84988651277
executive : 0.847549591563
chief : 0.842613979285
"""
