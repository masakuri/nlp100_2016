# coding=utf-8

"""
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""

# from nltk import stem
from stemming.porter2 import stem
import sys
import codecs
import argparse

def baseline(line, stop_list, feature_list):
    word_ls = line.split()
    # ストップワード除去
    for word in word_ls:
        if word in stop_list:
            word_ls = filter(lambda a: a != word, word_ls)
    # ステミング
    for i in range(len(word_ls)):
        word_ls[i] = stem(word_ls[i].strip())
    return word_ls

def all_features(line, stop_list, feature_list):
    word_ls = baseline(line, stop_list, feature_list)
    # bigram作成
    for i in range(1, len(word_ls)-1):
        word_ls.append("{}_{}".format(word_ls[i], word_ls[i+1]))
    return word_ls

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("-f", "--feature", dest = "feature", help = "input a or b, a : all features, b : baseline")
    args = p.parse_args()

    with codecs.open("stop_word.txt", encoding="latin1") as f:  # 文字化けへの対処
        feature_list = list()
        stop_list = f.read().strip().split(",")
        text = sys.stdin
        if args.feature == "a":
            for line in text:
                print " ".join(all_features(line, stop_list, feature_list))
        elif args.feature == "b":
            for line in text:
                print " ".join(baseline(line, stop_list, feature_list))
"""
$ python mk72.py -f b < sentiment.txt > baseline.txt
$ python mk72.py -f a < sentiment.txt > train.txt
"""
