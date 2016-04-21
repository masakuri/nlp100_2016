# coding=utf-8

"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""

import mk30

for line in mk30.load_morph():
    if line["pos1"] == "サ変接続":
        print line["surface"]

"""
$ python mk33.py
見当
記憶
話
装飾
突起
運転
記憶
分別
決心
我慢
餓死
訪問
始末
猶予
遭遇
我慢
記憶
返報
勉強
勉強
昼寝
珍重
昼寝
経験
供
供
...
"""
