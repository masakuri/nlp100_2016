# coding=utf-8

"""
62. KVS内の反復処理
60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
"""

import plyvel

db = plyvel.DB("artist.ldb", create_if_missing=True)
cnt = 0
for k, v in db:
    if v == "Japan":
        cnt += 1
print cnt

"""
$ python mk62.py
22128
"""
