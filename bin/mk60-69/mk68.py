# coding=utf-8

"""
68. ソート
"dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．
"""

import pymongo

client = pymongo.MongoClient()
db = client.MusicBrainz
collection = db.artist

dance_rate_artist = list()
for artist in collection.find({u"tags.value": "dance"}):
    if "rating" in artist:
        dance_rate_artist.append([artist["name"], artist["rating"]["count"]])
sorted_dance_rate_artist = sorted(dance_rate_artist, key=lambda x:x[1], reverse=True)
c = 0
for artist in sorted_dance_rate_artist:
    if c < 10:
        print artist[0].encode('utf_8'), artist[1]
        c += 1
    else:
        break

"""
$ python mk68.py
Madonna 26
Björk 23
The Prodigy 23
Rihanna 15
Britney Spears 13
Maroon 5 11
Adam Lambert 7
Fatboy Slim 7
Basement Jaxx 6
Cornershop 5
"""
