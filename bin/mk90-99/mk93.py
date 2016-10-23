# coding=utf-8

"""
93. アナロジータスクの正解率の計算
92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．
"""

import sys

analogy = sys.stdin
true_count = 0.0
false_count = 0.0
for line in analogy:
    ana_ls = line.rstrip().split(" ")
    if len(ana_ls) < 6:
        continue
    else:
        if ana_ls[3] == ana_ls[4]:
            true_count += 1.0
        else:
            false_count += 1.0

accracy = true_count / (true_count + false_count)
print str(accracy) + " " + "({}/{})".format(int(true_count), int(true_count + false_count))

"""
$ python mk93.py < analogy85.txt
0.0 (0/342)
$ python mk93.py < analogy90.txt
0.062656641604 (25/399)
"""

"""
$ python mk93.py < analogy85_10.txt
0.012987012987 (6/462)
$ python mk93.py < analogy90_10.txt
0.114624505929 (58/506)
"""
# 1/10
