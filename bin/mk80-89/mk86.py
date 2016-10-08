# coding=utf-8
"""
86. 単語ベクトルの表示
85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．
"""
import sys
import sklearn.decomposition as decomp
from sklearn.externals import joblib
import cPickle as pickle

search_word = sys.argv[1]
word_vectors = joblib.load(sys.argv[2]) # 単語の意味ベクトル読み込み
word_dic = pickle.load(sys.stdin)
search_word = search_word.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_") # United States -> United_States
try:
    print word_vectors[word_dic[search_word]]
except: # 単語が存在しない場合
    print "Error : no such target word."

"""
$ time python mk86.py "United States" "word_vectors.dump" < word_dic.pkl
[  2.00423029e+01  -7.17213470e+00  -3.73486024e+00  -9.04726798e-02
  -2.35693704e+00   2.13245641e+00   6.45408133e-01  -1.09712273e-01
...
  2.45453149e-04   3.66876167e-03   1.83225717e-03  -3.93640404e-03]
python mk86.py "United States" < word_dic.pkl  0.68s user 1.83s system 67% cpu 3.726 total
メモリ：600Mくらい？
"""
