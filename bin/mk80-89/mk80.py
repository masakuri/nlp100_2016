# coding=utf-8

"""
80. コーパスの整形
文を単語列に変換する最も単純な方法は，空白文字で単語に区切ることである． ただ，この方法では文末のピリオドや括弧などの記号が単語に含まれてしまう． そこで，コーパスの各行のテキストを空白文字でトークンのリストに分割した後，各トークンに以下の処理を施し，単語から記号を除去せよ．

トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"
空文字列となったトークンは削除
以上の処理を適用した後，トークンをスペースで連結してファイルに保存せよ．
"""

import sys

wiki_data = sys.stdin   # wikipedia記事読み込み
token_ls = list()
for line in wiki_data:
    word_ls = line.strip("\n").split(" ")
    for w in word_ls:
        token = w.strip(".,!?;:\(\)\[\]\'\"")   # 記号除去
        if token == "": # 空文字列となったトークン削除
            continue
        token_ls.append(token)
    print " ".join(token_ls)
    token_ls = list()

"""
$ time bzcat ../../data/enwiki-20150112-400-r100-10576.txt.bz2| python mk80.py | gzip > enwiki.txt.gz
bzcat ../../data/enwiki-20150112-400-r100-10576.txt.bz2  6.28s user 0.07s system 43% cpu 14.736 total
python mk80.py  12.87s user 0.16s system 88% cpu 14.750 total
gzip > enwiki.txt.gz  6.56s user 0.10s system 45% cpu 14.761 total
$ zcat enwiki.txt.gz | less
Anarchism

Anarchism is a political philosophy that advocates stateless societies often defined as self-governed voluntary institutions but that several authors have defined as more specific institutions based on non-hierarchical free associations Anarchism holds the state to be undesirable unnecessary or harmful While anti-statism is central anarchism entails opposing authority or hierarchical organisation in the conduct of human relations including but not limited to the state system
As a subtle and anti-dogmatic philosophy anarchism draws...
"""

"""
$ time bzcat ../../data/enwiki-20150112-400-r10-105752.txt.bz2| python mk80.py | gzip > enwiki10.txt.gz
bzcat ../../data/enwiki-20150112-400-r10-105752.txt.bz2  67.83s user 0.73s system 43% cpu 2:38.64 total
python mk80.py  131.08s user 1.24s system 83% cpu 2:38.63 total
gzip > enwiki10.txt.gz  66.29s user 1.05s system 42% cpu 2:38.62 total
"""
# 1/10
