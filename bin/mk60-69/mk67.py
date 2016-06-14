# coding=utf-8

"""
67. 複数のドキュメントの取得
特定の（指定した）別名を持つアーティストを検索せよ．
"""

import pymongo

client = pymongo.MongoClient()
db = client.MusicBrainz
collection = db.artist

for aliases in collection.find({"aliases.name": "Queen"}):
    print aliases

"""
$ python mk67.py
{u'name': u'Queen', u'area': u'Japan', u'gender': u'Female', u'tags': [{u'count': 1, u'value': u'kamen rider w'}, {u'count': 1, u'value': u'related-akb48'}], u'sort_name': u'Queen', u'ended': True, u'gid': u'420ca290-76c5-41af-999e-564d7c71f1a7', u'_id': ObjectId('575e5734b08a6b03fea3981a'), u'type': u'Character', u'id': 701492, u'aliases': [{u'name': u'Queen', u'sort_name': u'Queen'}]}
"""
