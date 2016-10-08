# coding=utf-8

"""
82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．

ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
"""

import random
import sys

data = sys.stdin
num = [1, 2, 3, 4, 5]

for i, line in enumerate(data): # コーパスの各行に対して
    words = line.rstrip("\n").split(" ")    # 各行を単語のリストにして
    for j, word in enumerate(words):    # 単語のリストの各単語に対して
        width = random.choice(num)  # 1~5の範囲で数字をランダムにチョイス
        for k in range(width, 0, -1):   # k = width, width -1 , ..., 1（単語tの前width単語）
            if j - k < 0:   # ターゲット単語のk個前に単語がなければパス
                continue
            else:
                print "{} {}".format(word, words[j - k])
        for k in range(1, width + 1):   # k = 1, 2, ..., width（単語tの後width単語）
            if j + k > len(words) - 1:  # ターゲット単語のk個先に単語がなければパス
                break
            else:
                print "{} {}".format(word, words[j + k])

"""
$ time zcat enwiki_countryname.txt.gz| python mk82.py| gzip > enwiki_context.txt.gz
(it took about 145s. (local)
$ zcat enwiki_context.txt.gz | less
Anarchism is
is Anarchism
is a
is political
is philosophy
a Anarchism
a is
a political
a philosophy
...
"""
