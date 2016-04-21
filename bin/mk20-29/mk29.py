# coding=utf-8

import mk28
import urllib, urllib2
import re, json

for k, v in mk28.remove_mark().iteritems():
    if "国旗画像" in k:
        image = v

url = "https://en.wikipedia.org/w/api.php?"
params = urllib.urlencode(
[("action", "query"),
("format", "json"),
("titles", "File:" + image),
("prop", "imageinfo"),
("iiprop", "url"),]
)

image_url = urllib.urlopen(url + params)
data = json.loads(image_url.read())
ls = data[u"query"][u"pages"].keys()
print data[u"query"][u"pages"][ls[0]][u"imageinfo"][0][u"url"]
# print data[u"query"][u"pages"]["-1"][u"imageinfo"][0][u"url"]


"""
> python mk29.py
https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg
"""
