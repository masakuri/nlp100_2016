# coding=utf-8

"""
78. 5分割交差検定
76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．
"""

# ベースライン
"""
$ classias-train -tb -g5 -x baseline.txt
Classias 1.1.1 trainer Copyright (c) 2008,2009 Naoaki Okazaki

Task type: binary
Training algorithm: lbfgs.logistic
Instance shuffle: false
Bias feature value: 1
Model file:
Instance splitting: 5
Holdout group: -1
Cross validation: true
Attribute filter:
Start time: 2016-09-01T15:14:04Z

Reading the data set from 1 files
- 1: baseline.txt
Number of instances: 10662
Number of groups: 5
Number of attributes: 15711
Number of labels: 2
Number of features: 15711
Seconds required: 0.102299

===== Cross validation (1/5) =====
Binary logistic regression using L-BFGS
c1: 0
c2: 1
num_memories: 6
epsilon: 1e-05
stop: 10
delta: 1e-05
max_iterations: 2147483647
linesearch: MoreThuente
max_linesearch: 20
lbfgs.regularization_start: 1

***** Iteration #1 *****
Loss: 5838.26
Feature L2-norm: 0.369064
Error norm: 904.428
Active features: 12924 / 15711
Line search trials: 2
Line search step: 0.000917801
Seconds required for this iteration: 0.008192
Accuracy: 0.5968 (1273/2133)
Micro P, R, F1: 0.5621 (959/1706), 0.8946 (959/1072), 0.6904

...

***** Iteration #94 *****
Loss: 3264.38
Feature L2-norm: 27.8917
Error norm: 1.32396
Active features: 14077 / 15711
Line search trials: 1
Line search step: 1
Seconds required for this iteration: 0.003605
Accuracy: 0.7570 (1614/2132)
Micro P, R, F1: 0.7539 (821/1089), 0.7666 (821/1071), 0.7602

L-BFGS terminated with the stopping criteria
Seconds required: 0.36471

Finish time: 2016-09-01T15:15:04Z
"""

# 全素性（ベースライン + 2-gram）
"""
$ classias-train -tb -g5 -x train.txt
Classias 1.1.1 trainer Copyright (c) 2008,2009 Naoaki Okazaki

Task type: binary
Training algorithm: lbfgs.logistic
Instance shuffle: false
Bias feature value: 1
Model file:
Instance splitting: 5
Holdout group: -1
Cross validation: true
Attribute filter:
Start time: 2016-09-01T15:17:23Z

Reading the data set from 1 files
- 1: train.txt
Number of instances: 10662
Number of groups: 5
Number of attributes: 109459
Number of labels: 2
Number of features: 109459
Seconds required: 0.281201

===== Cross validation (1/5) =====
Binary logistic regression using L-BFGS
c1: 0
c2: 1
num_memories: 6
epsilon: 1e-05
stop: 10
delta: 1e-05
max_iterations: 2147483647
linesearch: MoreThuente
max_linesearch: 20
lbfgs.regularization_start: 1

***** Iteration #1 *****
Loss: 5807.15
Feature L2-norm: 0.480917
Error norm: 1119.85
Active features: 87609 / 109459
Line search trials: 2
Line search step: 0.00108415
Seconds required for this iteration: 0.026852
Accuracy: 0.5926 (1264/2133)
Micro P, R, F1: 0.5584 (971/1739), 0.9058 (971/1072), 0.6909

...

***** Iteration #89 *****
Loss: 2319.24
Feature L2-norm: 30.5637
Error norm: 0.70611
Active features: 91152 / 109459
Line search trials: 1
Line search step: 1
Seconds required for this iteration: 0.016465
Accuracy: 0.7580 (1616/2132)
Micro P, R, F1: 0.7562 (819/1083), 0.7647 (819/1071), 0.7604

L-BFGS terminated with the stopping criteria
Seconds required: 1.49587

Finish time: 2016-09-01T15:16:20Z
"""
