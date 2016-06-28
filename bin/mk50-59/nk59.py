# coding=utf-8

"""
58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．

・述語: nsubj関係とdobj関係の子（dependant）を持つ単語
・主語: 述語からnsubj関係にある子（dependent）
・目的語: 述語からdobj関係にある子（dependent）
"""

"""
文明の利器ver.
"""


import xml.etree.ElementTree as ET
import sys
from nltk.tree import Tree

tree = ET.parse(sys.stdin)
elem = tree.getroot()
parse = elem.findall(".//parse")

"""
<parse>(ROOT (S (PP (NP (JJ Natural) (NN language) (NN processing)) (IN From) (NP (NNP Wikipedia))) (, ,) (NP (NP (DT the) (JJ free) (NN encyclopedia) (JJ Natural) (NN language) (NN processing)) (PRN (-LRB- -LRB-) (NP (NN NLP)) (-RRB- -RRB-))) (VP (VBZ is) (NP (NP (NP (DT a) (NN field)) (PP (IN of) (NP (NN computer) (NN science)))) (, ,) (NP (JJ artificial) (NN intelligence)) (, ,) (CC and) (NP (NP (NNS linguistics)) (VP (VBN concerned) (PP (IN with) (NP (NP (DT the) (NNS interactions)) (PP (IN between) (NP (NP (NNS computers)) (CC and) (NP (JJ human) (-LRB- -LRB-) (JJ natural) (-RRB- -RRB-) (NNS languages)))))))))) (. .))) </parse>
"""


for line in parse:
    tree = Tree.fromstring(line.text)
    for s in tree.subtrees():
        if s.label() == "NP":
            print " ".join(s.leaves())

"""
$ python smk59.py < nlp.txt.out
Natural language processing
Wikipedia
the free encyclopedia Natural language processing -LRB- NLP -RRB-
the free encyclopedia Natural language processing
NLP
a field of computer science , artificial intelligence , and linguistics concerned with the interactions between computers and human -LRB- natural -RRB- languages
a field of computer science
a field
computer science
artificial intelligence
linguistics concerned with the interactions between computers and human -LRB- natural -RRB- languages
linguistics
the interactions between computers and human -LRB- natural -RRB- languages
the interactions
computers and human -LRB- natural -RRB- languages
computers
human -LRB- natural -RRB- languages
...
"""
