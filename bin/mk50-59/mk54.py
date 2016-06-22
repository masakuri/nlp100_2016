# coding=utf-8

"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
"""

import xml.etree.ElementTree as ET
import sys

tree = ET.parse(sys.stdin)
elem = tree.getroot()
for w, l, p in zip(elem.findall(".//word"), elem.findall(".//lemma"), elem.findall(".//POS")):
    print "{}\t{}\t{}".format(w.text, l.text, p.text)

"""
$ python mk54.py < nlp.txt.out
Natural natural JJ
language        language        NN
processing      processing      NN
From    from    IN
Wikipedia       Wikipedia       NNP
,       ,       ,
the     the     DT
free    free    JJ
encyclopedia    encyclopedia    NN
Natural natural JJ
language        language        NN
processing      processing      NN
-LRB-   -lrb-   -LRB-
NLP     nlp     NN
-RRB-   -rrb-   -RRB-
is      be      VBZ
a       a       DT
field   field   NN
of      of      IN
computer        computer        NN
science science NN
,       ,       ,
artificial      artificial      JJ
intelligence    intelligence    NN
,       ,       ,
and     and     CC
linguistics     linguistics     NNS
concerned       concern VBN
with    with    IN
the     the     DT
interactions    interaction     NNS
between between IN
computers       computer        NNS
and     and     CC
human   human   JJ
-LRB-   -lrb-   -LRB-
natural natural JJ
-RRB-   -rrb-   -RRB-
languages       language        NNS
.       .       .
...
"""
