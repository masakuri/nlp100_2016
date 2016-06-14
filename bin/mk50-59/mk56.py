# coding=utf-8

"""
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
"""

import xml.etree.ElementTree as ET
import sys, re

tree = ET.parse(sys.stdin)
elem = tree.getroot()
sentences = elem.findall(".//tokens")
word_ls = list()
sentences_ls = list()

# トークンを収集し，文ごとにリスト化
for tokens in sentences:
    for token in tokens:
        word_ls.append(token.find("word").text)
    sentences_ls.append(" ".join(word_ls))
    word_ls = list()

# coreference情報を収集し，[文のid, 代表参照表現, 参照表現]のリスト作成
coreferences = elem.findall(".//coreference")
rep_coref_list = list()
mention_list = list()
for coreference in coreferences:
    for mention in coreference:
        if mention.attrib.get("representative") == "true":
            rep_coref_list.append(mention.find("sentence").text)
            rep_coref_list.append(mention.find("text").text)
            rep_coref_list.append(coreference[1].find("text").text)
            mention_list.append(rep_coref_list)
            rep_coref_list = list()

# 参照表現（mention）を代表参照表現（representative mention）に置換
for ment in mention_list:
    repl = "「" + ment[1] + "（" + ment[2] + "）" + "」"
    sentences_ls[int(ment[0])-1] = re.sub(ment[1], repl, sentences_ls[int(ment[0])-1])

for sentence in sentences_ls:
    print sentence

"""
$ python mk56.py < nlp.txt.out
Natural language processing From Wikipedia , 「the free encyclopedia Natural language processing -LRB- NLP -RRB-（a field of computer science）」 is a field of computer science , artificial intelligence , and linguistics concerned with the interactions between 「computers（computers）」 and human -LRB- natural -RRB- languages .
As such , NLP is related to the area of humani-computer interaction .
Many challenges in NLP involve natural language understanding , that is , enabling computers to derive meaning from human or natural language input , and others involve natural language generation .
History The history of 「NLP（NLP）」 generally starts in the 1950s , although work can be found from earlier periods .
In 1950 , 「Alan Turing（Turing）」 published an article titled `` Computing Machinery and Intelligence '' which proposed what is now called the Turing test as a criterion of intelligence .
...
"""
