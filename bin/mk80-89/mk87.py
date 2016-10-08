# coding=utf-8
"""
87. 単語の類似度
85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．
"""
import sys
from sklearn.externals import joblib
import cPickle as pickle
import numpy as np

target_word = sys.argv[1]
search_word = sys.argv[2]
word_vectors = joblib.load("word_vectors.dump")
word_dic = pickle.load(sys.stdin)
target_word = target_word.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_") # United States ->  United_States
search_word = search_word.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_") # U.S. -> U.S

try:
    v1 = word_vectors[word_dic[target_word]]
    v2 = word_vectors[word_dic[search_word]]
    cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))    # コサイン類似度計算
    print cos_sim
except:
    print "Error : no such target word or search word."

"""
$ time python mk87.py "United States" "U.S." < word_dic.pkl
0.911171578711
python mk87.py "United States" "U.S." < word_dic.pkl  0.36s user 1.69s system 73% cpu 2.773 total
メモリ：150Mくらい？
"""
