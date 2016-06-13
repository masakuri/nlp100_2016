# coding=utf-8

"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""

"""
(/usr/local/lib/stanford-corenlp-full-2015-12-09/ディレクトリ内で)
$ java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file nlp.txt
-> nlp.txt.outのXMLファイル
"""

from xml.etree.ElementTree import *
import sys

tree = parse(sys.stdin)
elem = tree.getroot()
for e in elem.findall(".//word"):
    print e.text

"""
$ python mk53.py < nlp.txt.out
Natural
language
processing
From
Wikipedia
,
the
free
encyclopedia
Natural
language
processing
-LRB-
NLP
-RRB-
is
a
field
of
computer
science
,
artificial
intelligence
,
and
linguistics
concerned
with
the
interactions
between
computers
and
human
-LRB-
natural
-RRB-
languages
.
...
"""
