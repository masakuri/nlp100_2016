# coding=utf-8

"""
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
"""

"""
$ cat baseline.txt | classias-tag -m baseline.model -p -r | sed s/"\s"/"\t"/g | sed s/":"/"\t"/g > result_base.txt
$ less result_base.txt
+1      +1      0.905429
+1      +1      0.92876
-1      -1      0.247264
+1      +1      0.616035
-1      -1      0.209783
...
$ cat train.txt | classias-tag -m train.model -p -r | sed s/"\s"/"\t"/g | sed s/":"/"\t"/g > result_all.txt
$ less result_all.txt
+1      +1      0.935193
+1      +1      0.935933
-1      -1      0.119766
+1      +1      0.740225
-1      -1      0.134418
...
"""
