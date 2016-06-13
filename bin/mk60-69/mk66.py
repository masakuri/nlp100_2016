# coding=utf-8

"""
66. 検索件数の取得
MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．
"""

"""
$ mongo
MongoDB shell version: 3.2.4
connecting to: test
> use MusicBrainz
switched to db MusicBrainz
> db.artist.find({area: "Japan"}).count()
22821
"""
# mk62の出力と値が異なるのはなぜ？

import pymongo

client = pymongo.MongoClient()
db = client.MusicBrainz
collection = db.artist
print collection.find({"area": "Japan"}).count()

"""
$ python mk66.py
22821
"""
