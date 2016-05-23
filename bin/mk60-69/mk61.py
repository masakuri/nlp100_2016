# coding=utf-8

"""
61. KVSの検索
60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．
"""

import plyvel
import sys

db = plyvel.DB("artist.ldb", create_if_missing=True)
query = sys.argv[1]
print db.get(query)

"""
$ python mk61.py Oasis
United Kingdom
$ python mk61.py Michael Jackson
United States
$python mk61.py 美空ひばり
Japan
$python mk61.py Masakuri
None
"""
