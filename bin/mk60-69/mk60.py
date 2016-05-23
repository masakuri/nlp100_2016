# coding=utf-8

"""
60. KVSの構築
Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．
"""

import json
import plyvel
import sys

data = sys.stdin
db = plyvel.DB('artist.ldb',create_if_missing=True)

for line in data:
    jsonData = json.loads(line)
    if "name" in jsonData and "area" in jsonData:
        db.put(jsonData["name"].encode("utf_8"), jsonData["area"].encode("utf_8"))
db.close()

"""
$ gzcat artist.json.gz | python mk60.py
"""
