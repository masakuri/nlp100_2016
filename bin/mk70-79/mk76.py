# coding=utf-8

"""
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
"""

"""
$ cat baseline.txt | classias-tag -m baseline.model -p -r | sed s/"\s"/"\t"/g | sed s/":"/"\t"/g > result_base.txt
$ less result_base.txt
-1      -1      0.0826453
-1      -1      0.12925
-1      -1      0.0559257
+1      +1      0.883182
+1      +1      0.668342
-1      -1      0.166365
+1      +1      0.947731
+1      +1      0.720695
-1      -1      0.358625
+1      +1      0.833021
...
$ cat train.txt | classias-tag -m train.model -p -r | sed s/"\s"/"\t"/g | sed s/":"/"\t"/g > result_all.txt
$ less result_all.txt
-1      -1      0.0179921
-1      -1      0.0960401
-1      -1      0.0643568
+1      +1      0.930163
+1      +1      0.79272
-1      -1      0.0936229
+1      +1      0.95576
+1      +1      0.858038
-1      -1      0.297911
+1      +1      0.893934
"""