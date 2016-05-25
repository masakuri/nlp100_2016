# coding=utf-8

"""
63. オブジェクトを値に格納したKVS
KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
"""

import gzip, json
import plyvel
import sys

def create_database(data):
    db = plyvel.DB('artist_tags.ldb',create_if_missing=True)
    tag_ls = list()
    tags_ls = list()

    for line in data:
        jsonData = json.loads(line)
        if "name" in jsonData and "tags" in jsonData:
            db.put(jsonData["name"].encode("utf_8"), json.dumps(jsonData["tags"]).encode("utf_8"))

    db.close()

def search_tag(artist):
    db = plyvel.DB("artist_tags.ldb", create_if_missing=True)
    if db.get(artist) == None:
        print "None"
    else:
        for tag in json.loads(db.get(artist)):
            print "tag : " + tag["value"] + ", " + "count : " + str(tag["count"])

if __name__ == '__main__':
    option = raw_input("create database (input 0) or seach tags (input 1) ? : ")
    if option == "0":
        file_name = raw_input("input file name : ")
        data = gzip.open(file_name)
        create_database(data)
    elif option == "1":
        artist = raw_input("input artist name : ")
        search_tag(artist)

"""
$ python mk63.py
create database (input 0) or seach tags (input 1) ? : 0
input file name : ../../data/artist.json.gz
$ python mk63.py
create database (input 0) or seach tags (input 1) ? : 1
input artist name : Oasis
tag : rock, count : 1
tag : britpop, count : 3
tag : british, count : 4
tag : uk, count : 1
tag : britannique, count : 1
tag : rock and indie, count : 1
tag : england, count : 1
tag : manchester, count : 1
$ python mk63.py
create database (input 0) or seach tags (input 1) ? : 1
input artist name : Masakuri
None
"""
