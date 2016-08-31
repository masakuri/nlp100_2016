#!/usr/local/bin/python
# coding=utf-8

"""
69. Webアプリケーションの作成
ユーザから入力された検索条件に合致するアーティストの情報を表示するWebアプリケーションを作成せよ．アーティスト名，アーティストの別名，タグ等で検索条件を指定し，アーティスト情報のリストをレーティングの高い順などで整列して表示せよ．
"""

# CGIだけバージョン

import sys
sys.path.append("/Library/Python/2.7/site-packages")
import cgi
import cgitb; cgitb.enable()
import pymongo

if __name__ == '__main__':

    print "Content-Type: text/html; charset=utf-8"
    print ''

    client = pymongo.MongoClient()
    db = client.MusicBrainz
    collection = db.artist

    # クエリの取得
    option = ""
    query = ""
    form = cgi.FieldStorage()
    if form.has_key('option') and form.has_key('query'):
        option = form['option'].value
        query = form['query'].value

    # optionで選択されたものをDBから取ってくる
    if option == "tags":
        artists = collection.find({'tags.value':query}).sort('rating.count',pymongo.DESCENDING)
    elif option == "name":
        artists = collection.find({"name": query}).sort('rating.count',pymongo.DESCENDING)
    elif option == "aliases":
        artists = collection.find({"aliases.name": query}).sort('rating.count',pymongo.DESCENDING)
    elif option == "area":
        artists = collection.find({"area": query}).sort('rating.count',pymongo.DESCENDING)

    # HTMLの書き出し
    print '<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8"><title>MusicBrainzでのWebアプリケーション作成</title></head><body><h2>「%s, %s」に関連するアーティスト</h2><form name = "Form1" method="POST" action="/cgi-bin/mk_cgi69.py">INPUT "name", "aliases", "tags", or "area" : <input type="text" name="option" value="%s"><p>INPUT query : <input type="text" name="query" value="%s"><p><input type="submit" value="一覧で表示"><p></form><table></tr>'%(option, query, option, query)

    # optionそれぞれの結果出力
    if option == "tags":
        if artists.count() > 0:
            print "<tr><th>アーティスト</th><th>レーティング</th><th>タグ</th></tr>"
            for artist in artists:
                tag_ls = list()
                for i in range(len(artist.get("tags"))):
                    tag_ls.append(artist.get("tags")[i].get("value").encode("utf8"))
                if artist.has_key("rating"):
                    print '<tr><td>%s</td><td>%d</td><td>%s</td></tr>'%(artist.get("name").encode("utf8"), artist.get("rating").get("count"), " | ".join(tag_ls[:5]))
                else:
                    print '<tr><td>%s</td><td>None</td><td>%s</td></tr>'%(artist.get("name").encode("utf8"), " | ".join(tag_ls[:5]))
        else:
            print "<td>タグが「%s」のアーティストはいません</td>"%(query)

    elif option == "name":
        if artists.count() > 0:
            print "<tr><th>アーティスト</th><th>地域</th><th>タグ</th></tr>"
            for artist in artists:
                if artist.has_key("tags"):
                    tag_ls = list()
                    for i in range(len(artist.get("tags"))):
                        tag_ls.append(artist.get("tags")[i].get("value"))
                    print '<tr><td>%s</td><td>%s</td><td>%s</td></tr>'%(artist.get("name").encode("utf8"), artist.get("area"), " | ".join(tag_ls[:10]))
                else:
                    print '<tr><td>%s</td><td>%s</td><td>None</td></tr>'%(artist.get("name").encode("utf8"), artist.get("area"))
        else:
            print "<td>アーティスト名が「%s」のアーティストはいません</td>"%(query)

    elif option == "aliases":
        if artists.count() > 0:
            print "<tr><th>アーティスト</th><th>地域</th><th>タグ</th></tr>"
            for artist in artists:
                if artist.has_key("tags"):
                    tag_ls = list()
                    for i in range(len(artist.get("tags"))):
                        tag_ls.append(artist.get("tags")[i].get("value"))
                    print '<tr><td>%s</td><td>%s</td><td>%s</td></tr>'%(artist.get("name").encode("utf8"), artist.get("area"), " | ".join(tag_ls[:10]))
                else:
                    print '<tr><td>%s</td><td>%s</td><td>None</td></tr>'%(artist.get("name").encode("utf8"), artist.get("area").encode("utf8"))
        else:
            print "<td>別名が「%s」のアーティストはいません</td>"%(query)

    elif option == "area":
        if artists.count() > 0:
            print "<tr><th>アーティスト</th><th>レーティング</th><th>タグ</th></tr>"
            for artist in artists:
                if artist.has_key("tags"):
                    tag_ls = list()
                    for i in range(len(artist.get("tags"))):
                        tag_ls.append(artist.get("tags")[i].get("value").encode("utf8"))
                    if artist.has_key("rating"):
                        print '<tr><td>%s</td><td>%d</td><td>%s</td></tr>'%(artist.get("name").encode("utf8"), artist.get("rating").get("count"), " | ".join(tag_ls[:5]))
                    else:
                        print '<tr><td>%s</td><td>None</td><td>%s</td></tr>'%(artist.get("name").encode("utf8"), " | ".join(tag_ls[:5]))
                else:
                    print '<tr><td>%s</td><td>%d</td><td>None</td></tr>'%(artist.get("name").encode("utf8"), artist.get("rating").get("count"))
        else:
            print "<td>地域が「%s」のアーティストはいません</td>"%(query)
    else:
        print "<td>ERROR</td>"

    print '</table></body></html>'

"""
cgi-binディレクトリのあるディレクトリ下で
$ python -m CGIHTTPServer
URLにhttp://localhost:8000/cgi-bin/mk_cgi69.pyで実行可能
パーミッション設定：
$ chmod 755 mk_cgi69.py
"""
