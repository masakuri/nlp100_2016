# coding=utf-8

"""
91. アナロジーデータの準備
単語アナロジーの評価データをダウンロードせよ．このデータ中で": "で始まる行はセクション名を表す．例えば，": capital-common-countries"という行は，"capital-common-countries"というセクションの開始を表している．ダウンロードした評価データの中で，"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．
"""

# 単語アナロジーの評価データ：https://github.com/arfon/word2vec/blob/master/questions-words.txt

import sys

data = sys.stdin
flag = 0
target = sys.argv[1]

for line in data:
    if line.startswith(":") and flag == 0:
        section = line.rstrip()
    if line.startswith(":") and flag == 1:
        break
    if section == ": " + target:
        flag == 1
        print line,

"""
$ python mk91.py family < ~/word2vec/questions-words.txt > family.txt
$ less family.txt
: family
boy girl brother sister
boy girl brothers sisters
boy girl dad mom
boy girl father mother
boy girl grandfather grandmother
...
brother sister brothers sisters
brother sister dad mom
brother sister father mother
brother sister grandfather grandmother
brother sister grandpa grandma
brother sister grandson granddaughter
...
"""
