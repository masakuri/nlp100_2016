# coding=utf-8

"""
90. word2vecによる学習
81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
"""

"""
$ time ~/word2vec/word2vec -train ../mk80-89/enwiki_countryname.txt -output w2v.txt -size 300
Starting training using file ../mk80-89/enwiki_countryname.txt
Vocab size: 85470
Words in train file: 11703449
Alpha: 0.000026  Progress: 99.98%  Words/thread/sec: 155.78k  ~/word2vec/word2vec -train ../mk80-89/enwiki_countryname.txt -output w2v.txt   391.01s user 3.87s system 298% cpu 2:12.28 total
"""

"""
Starting training using file ../mk80-89/enwiki_countryname10.txt
Vocab size: 361919
Words in train file: 120903783
Alpha: 0.000021  Progress: 99.96%  Words/thread/sec: 153.58k  ~/word2vec/word2vec -train ../mk80-89/enwiki_countryname10.txt -output  -size  4033.44s user 34.06s system 334% cpu 20:15.92 total
"""
# 1/10

import sys
from gensim.models import Word2Vec
import cPickle as pickle
import numpy as np
from sklearn.externals import joblib

model = Word2Vec.load_word2vec_format('w2v.txt', binary=False) # 初回実行時のみ
pickle.dump(model, open('w2v.dump', 'w'))  # 初回実行時のみ（約45s）
model = Word2Vec.load("w2v.dump")

word_dic = dict()
for index, word in enumerate(model.vocab.keys()):
    word_dic[word] = index
pickle.dump(word_dic, open('word_dic.pkl', 'w'))

word_vectors = np.ndarray((len(word_dic), 300))
for word, index in word_dic.iteritems():
    word_vectors[index] = model[word]
joblib.dump(word_vectors, "word_vectors.dump")

"""
$ time python mk090.py
python mk090.py  48.29s user 2.75s system 95% cpu 53.526 total

$ python ../mk80-89/mk86.py "United States" "word_vectors.dump" < word_dic.pkl
[-0.59289598 -0.112545   -0.31538901  0.86996502  1.36431003 -0.91765898
  1.12998402 -0.22202399  1.50643301 -0.44446301  0.02414     0.31549901
  ...
  -0.15607101 -0.112776   -0.97495699 -0.120624   -1.37801695 -0.78561598]

$ python ../mk80-89/mk87.py "United States" "U.S." "word_vectors.dump" < word_dic.pkl
0.778583733394

$ python ../mk80-89/mk88.py "England" "word_vectors.dump" < word_dic.pkl
England : 1.0
Scotland : 0.658398510344
Wales : 0.625836805319
Hampshire : 0.558257382749
Britain : 0.538927367237
Ireland : 0.534616221574
Somerset : 0.506487975891
Lancashire : 0.498837954903
Edinburgh : 0.487557999356
Plymouth : 0.482953042261

$ python ../mk80-89/mk89.py "Spain" "Madrid" "Athens" "word_vectors.dump" < word_dic.pkl
Spain : 0.716260083224
Athens : 0.693176488211
Greece : 0.53880390777
Egypt : 0.52901897955
Flanders : 0.52554186653
Portugal : 0.524977385419
Slovakia : 0.521552416423
Persia : 0.516802569374
Denmark : 0.516534803669
Armenia : 0.504713543969
"""
# mk90.pyと出力が微妙に違う

"""
$ python ../mk80-89/mk86.py "United States" "word_vectors10.dump" < word_dic10.pkl
[ -8.52648020e-01   8.57218981e-01   1.24187005e+00   8.44283998e-01
   1.51653007e-01   4.18433011e-01  -1.12193501e+00  -5.08320987e-01
   ...
   3.54476988e-01  -8.66167009e-01  -1.32056904e+00   7.47537971e-01]

$ python ../mk80-89/mk88.py "England" "word_vectors10.dump" < word_dic10.pkl
England : 1.0
Scotland : 0.646406283883
England's : 0.62198555362
Wales : 0.61287844449
Hampshire : 0.603327266618
Britain : 0.587887399797
France : 0.572107203253
Ireland : 0.559225604672
Buckinghamshire : 0.551524775092
Spain : 0.541347225325

$ python ../mk80-89/mk89.py "Spain" "Madrid" "Athens" "word_vectors10.dump" < word_dic10.pkl
Athens : 0.699001976392
Greece : 0.656641294854
Crete : 0.526037154243
Peloponnese : 0.524510227007
Spain : 0.510383282114
Egypt : 0.507665443556
Epirus : 0.502542425933
Chios : 0.500858933578
Cyprus : 0.496740746761
Persia : 0.483654790251

$ python ../mk80-89/mk89.py "King" "man" "woman" "word_vectors10.dump" < word_dic10.pkl
King : 0.792164559769
Queen : 0.63301437616
Princess : 0.555435822323
queen : 0.524056748856
king : 0.523562465674
Prince : 0.507010668523
princess : 0.501492818286
monarch : 0.48413300382
Liliuokalani : 0.481334553949
Tiye : 0.479282394488
"""
# 1/10
