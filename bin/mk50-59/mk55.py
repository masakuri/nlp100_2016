# coding=utf-8

"""
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
"""

import xml.etree.ElementTree as ET
import sys

tree = ET.parse(sys.stdin)
elem = tree.getroot()
for e in elem.getiterator("token"):
    if e.find("NER").text == "PERSON":
        print e.find("word").text

"""
$ python mk55.py < nlp.txt.out
Alan
Turing
Joseph
Weizenbaum
MARGIE
Schank
Wilensky
Meehan
Lehnert
Carbonell
Lehnert
Jabberwacky
Moore
"""
