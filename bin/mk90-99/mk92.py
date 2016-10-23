# coding=utf-8

"""
92. アナロジーデータへの適用
91で作成した評価データの各事例に対して，vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，そのベクトルと類似度が最も高い単語と，その類似度を求めよ．求めた単語と類似度は，各事例の末尾に追記せよ．このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
"""

import sys
from gensim.models import Word2Vec
from sklearn.externals import joblib
import cPickle as pickle
import numpy as np
from tqdm import tqdm

def cos_sim_max_word(v, word_dic, word_vectors):
    cos_sim_max_word = ""
    word_cos_sim = 0.0
    for word, index in word_dic.iteritems():
        vector = word_vectors[index]
        cos_sim_temp = np.dot(v, vector) / (np.linalg.norm(v) * np.linalg.norm(vector))    # コサイン類似度計算
        if word_cos_sim < cos_sim_temp:
            word_cos_sim = cos_sim_temp
            cos_sim_max_word = word
    # print cos_sim_max_word, word_cos_sim
    return cos_sim_max_word, word_cos_sim

def main():
    with open("family.txt") as f:
        word_vectors = joblib.load(sys.argv[1])
        word_dic = pickle.load(sys.stdin)
        for line in tqdm(f):
            if line.startswith(":"):
                continue
            else:
                words = line.rstrip().split()
                word1 = words[0]
                word2 = words[1]
                word3 = words[2]
                word4 = words[3]

                try:    # 1/100でやるとgrandpaとかがなくてエラーはくのでそれは無視
                    v1 = word_vectors[word_dic[word1]]
                    v2 = word_vectors[word_dic[word2]]
                    v3 = word_vectors[word_dic[word3]]

                    v = v2 - v1 + v3
                    # print v
                    w, cos_sim = cos_sim_max_word(v, word_dic, word_vectors)
                    print "{} {} {} {} {} {}".format(word1, word2, word3, word4, w, cos_sim)

                except:
                    print "{} {} {} {}".format(word1, word2, word3, word4)
                    continue

if __name__ == '__main__':
    main()

"""
$ time python mk92.py "word_vectors.dump" < word_dic.pkl > analogy90.txt
python mk92.py "word_vectors.dump" < word_dic.pkl > analogy90.txt  446.33s user 3.30s system 91% cpu 8:12.03 total
$ less analogy90.txt
boy girl brother sister brother 0.870648144913
boy girl brothers sisters brothers 0.82450440473
boy girl dad mom girl 0.72481973228
boy girl father mother father 0.876267723232
boy girl grandfather grandmother grandfather 0.767704640815
...

$ time python mk92.py "../mk80-89/word_vectors.dump" < ../mk80-89/word_dic.pkl > analogy85.txt
python mk92.py "../mk80-89/word_vectors.dump" < ../mk80-89/word_dic.pkl >   144.96s user 2.91s system 91% cpu 2:42.34 total
$ less analogy85.txt
boy girl brother sister brother 0.862055193971
boy girl brothers sisters brothers 0.886286842265
boy girl dad mom dad 0.773029551655
boy girl father mother father 0.848115211511
boy girl grandfather grandmother grandfather 0.856013372233
...
"""

"""
$ time python mk92.py "../mk80-89/word_vectors.dump" < ../mk80-89/word_dic.pkl > analogy85_10.txt
python mk92.py "../mk80-89/word_vectors.dump" < ../mk80-89/word_dic.pkl >   875.20s user 4.04s system 95% cpu 15:17.95 total

$ time python mk92.py "word_vectors10.dump" < word_dic10.pkl > analogy90_10.txt
python mk92.py "word_vectors10.dump" < word_dic10.pkl > analogy90_10.txt  2818.25s user 1.77s system 99% cpu 47:05.40 total
"""
# 1/10
