# coding=utf-8

"""
64. MongoDBの構築
アーティスト情報（artist.json.gz）をデータベースに登録せよ．さらに，次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value
"""

import pymongo
import json
import sys

data = sys.stdin

client = pymongo.MongoClient()
db = client.MusicBrainz
collection = db.artist

for line in data:
    jsonData = json.loads(line)
    collection.insert(jsonData)

collection.create_index([("name", pymongo.ASCENDING)])
collection.create_index([("aliases.name", pymongo.ASCENDING)])
collection.create_index([("tags.value", pymongo.ASCENDING)])
collection.create_index([("rating.value", pymongo.ASCENDING)])

"""
$ gzcat ../../data/artist.json.gz | python mk64.py
約6分でデータベース登録完了！
"""
