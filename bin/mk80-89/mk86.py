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

"""
[  2.11096797e+01   4.83857028e+00   1.17174274e+00   1.11480757e+00
  -2.29408570e-01   1.87327293e+00  -1.43141500e+00  -5.96348974e-01
  ...
  -1.18529204e-02  -3.07250694e-05  -5.37823405e-02   2.36480057e-01]
python mk86.py "United States" "word_vectors10.dump" < word_dic.pkl  0.47s user 2.78s system 8% cpu 39.749 total（martini01）
"""
# 1/10
