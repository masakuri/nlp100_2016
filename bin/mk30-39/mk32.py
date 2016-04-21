# coding=utf-8

"""
32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""

import mk30

for line in mk30.load_morph():
    if line["pos"] == "動詞":
        print line["base"]

"""
$ python mk32.py
生れる
つく
する
泣く
する
いる
始める
見る
聞く
捕える
煮る
食う
思う
載せる
られる
持ち上げる
られる
する
ある
落ちつく
...
"""
