# coding=utf-8

"""
74. 予測
73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．
"""

import sys
from stemming.porter2 import stem
from math import exp

def classfy(text, model):
    text = preprocess(text)
    text_word = text.split()
    weight = 0.0
    for line in model:
        weight_word = line.split()
        if weight_word[0] == "@classias":
            continue
        elif weight_word[1] == "__BIAS__":
            bias = float(weight_word[0])
        else:
            if weight_word[1] in text_word:
                weight += float(weight_word[0])
    weight_bias = weight + bias
    prob = 1/(1 + exp(weight_bias))
    if weight_bias > 0:
        return "{}\t{}".format("+1", prob)
    else:
        return "{}\t{}".format("-1", prob)

def preprocess(text):
    word_ls = text.split()
    # ステミング
    for i in range(len(word_ls)):
        word_ls[i] = stem(word_ls[i].strip())
    # bigram作成
    for i in range(1, len(word_ls)-1):
        word_ls.append("{}_{}".format(word_ls[i], word_ls[i+1]))
    return " ".join(word_ls)

if __name__ == '__main__':
    model = sys.stdin
    text = sys.argv[1]
    print classfy(text, model)

"""
$ python mk74.py "the movie is the worst one" < baseline.model
-1     	0.91398984577
$ python mk74.py "the movie is the worst one" < train.model
-1     	0.895386325565
$ python mk74.py "the movie is the best one" < baseline.model
-1     	0.533676213591
$ python mk74.py "the movie is the best one" < train.model
+1     	0.487546076434
"""
