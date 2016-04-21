# coding=utf-8

"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""

import mk30

for line in mk30.load_morph():
    if line["pos"] == "動詞":
        print line["surface"]

"""
$ python mk31.py
生れ
つか
し
泣い
し
いる
始め
見
聞く
捕え
煮
食う
思わ
載せ
られ
持ち上げ
られ
し
あっ
落ちつい
...
"""
