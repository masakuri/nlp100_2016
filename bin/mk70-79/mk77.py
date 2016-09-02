# coding=utf-8

"""
77. 正解率の計測
76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．
"""

import sys

result = sys.stdin
true_count = 0
false_count = 0
true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0

for line in result:
    label = line.split("\t")
    answer = label[0]
    predict = label[1]
    if answer == predict and predict == "+1":
        true_positive += 1
        true_count += 1
    elif answer == predict and predict == "-1":
        true_negative += 1
        true_count += 1
    elif answer != predict and predict == "+1":
        false_positive += 1
        false_count += 1
    elif answer != predict and predict == "-1":
        false_negative += 1
        false_count += 1

accuracy = float(true_count) / float((true_count + false_count))
precision = float(true_positive) / float((true_positive + false_positive))
recall = float(true_positive) / float((true_positive + false_negative))
f1 = 2.0 * precision * recall / (precision + recall)

print "accuracy : " + str(accuracy)
print "precision : " + str(precision)
print "recall : " + str(recall)
print "F1 : " + str(f1)

"""
$ python mk77.py < result_base.txt
accuracy : 0.927593322078
precision : 0.930175504812
recall : 0.924592009004
F1 : 0.927375352775
$ python mk77.py < result_all.txt
accuracy : 0.996623522791
precision : 0.997369904189
recall : 0.995873194523
F1 : 0.996620987423
"""

# コマンドラインで
"""
$ cat baseline.txt | classias-tag -m baseline.model -qt
Accuracy: 0.9276 (9890/10662)
Micro P, R, F1: 0.9302 (4929/5299), 0.9246 (4929/5331), 0.9274
$ cat train.txt | classias-tag -m train.model -qt
Accuracy: 0.9966 (10626/10662)
Micro P, R, F1: 0.9974 (5309/5323), 0.9959 (5309/5331), 0.9966
"""
