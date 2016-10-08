# coding=utf-8

"""
83の出力を利用し，単語文脈行列Xを作成せよ．
"""

import sys
from math import log
import scipy.sparse as sp
import cPickle as pickle

f = sys.stdin
word_buff = list()
f_tc_ls = list()
f_t_dic = dict()
f_c_dic = dict()
word_index = dict()
flag = 0
i = 0
for line in f:  # 一つのファイルにぶち込んだものを
    if "*****(f_tc)*****" in line:
        continue
    elif "*****(f_t)*****" in line:
        flag = 1
        continue
    elif "*****(f_c)*****" in line:
        flag = 2
        continue
    elif "*****N*****" in line:
        flag = 3
    elif flag == 0:
        f_tc_ls.append(line.rstrip("\n"))   # f(t, c)をリスト化（[d long 1, Manson Arctic 1, ...]）
    elif flag == 1:
        word, count = line.rstrip("\n").split(" ")
        f_t_dic[word] = count    # f(t)を辞書化（{biennials : 14, unsupportable : 2, ...}）
        word_index[word] = i
        i += 1
    elif flag == 2:
        word, count = line.rstrip("\n").split(" ")
        f_c_dic[word] = count   # f(c)を辞書化（{biennials : 16, unsupportable : 3, ...}）
    elif flag == 3:
        N = float(line)

tc_matrix = sp.lil_matrix((len(f_t_dic), len(f_c_dic)))   # 疎行列作成
word_dic = dict()
context_dic = dict()

for line in f_tc_ls:    # [d long 1, Manson Arctic 1, ...]の各要素に対して
    word, context, count = line.split(" ")
    if int(count) < 10: # 共起回数10未満は無視
        continue
    else:
        f_t = float(f_t_dic[word])
        f_c = float(f_c_dic[word])
        ppmi_tc = max(log(N * float(count) * 1.0 / (f_t * f_c), 2.0), 0.0)  # PPMI計算
        if ppmi_tc == 0.0: # PPMI = 0のものは無視
            continue
        else:
            word_dic[word] = word_index[word]   # {PPMIが0以上だった単語 : その単語のindex, ...}という辞書
            context_dic[context] = word_index[context]  # {PPMIが0以上だった文脈語 : その単語のindex, ...}という辞書
            tc_matrix[word_index[word], word_index[context]] = ppmi_tc  # (単語のindex, 文脈語のindex) = PPMIの行列
            print "{}\t{}\t{}".format(word, context, ppmi_tc)
pickle.dump(word_dic, open('word_dic.pkl', 'w'))
pickle.dump(context_dic, open('context_dic.pkl', 'w'))
pickle.dump(tc_matrix, open('wc_array.pkl', 'w'))

"""
$ time zcat enwiki_wordfreq.gz| python mk84.py | gzip > enwiki_wcarray.txt.gz
zcat enwiki_wordfreq.gz  4.69s user 0.24s system 13% cpu 35.498 total
python mk84.py  90.81s user 7.46s system 91% cpu 1:47.18 total
gzip > enwiki_wcarray.txt.gz  0.88s user 0.02s system 0% cpu 1:47.18 total
メモリ：1.5Gくらい
$ zcat enwiki_wcarray.txt.gz | less
wisdom  the     13.4807250823
total   played  2.410774014
Pacific Railroad        6.10480316866
handed  to      11.6679296753
sensitivity     the     12.6215080698
show    himself 0.37250394707
...
"""
