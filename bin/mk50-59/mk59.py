# coding=utf-8

"""
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．
"""

"""
ゴリ押しver.（頑張ったよ俺）
"""

import xml.etree.ElementTree as ET
import sys, re

tree = ET.parse(sys.stdin)
elem = tree.getroot()
cnt = 0
np_list = list()
result_list = list()
parse = elem.findall(".//parse")

"""
<parse>(ROOT (S (PP (NP (JJ Natural) (NN language) (NN processing)) (IN From) (NP (NNP Wikipedia))) (, ,) (NP (NP (DT the) (JJ free) (NN encyclopedia) (JJ Natural) (NN language) (NN processing)) (PRN (-LRB- -LRB-) (NP (NN NLP)) (-RRB- -RRB-))) (VP (VBZ is) (NP (NP (NP (DT a) (NN field)) (PP (IN of) (NP (NN computer) (NN science)))) (, ,) (NP (JJ artificial) (NN intelligence)) (, ,) (CC and) (NP (NP (NNS linguistics)) (VP (VBN concerned) (PP (IN with) (NP (NP (DT the) (NNS interactions)) (PP (IN between) (NP (NP (NNS computers)) (CC and) (NP (JJ human) (-LRB- -LRB-) (JJ natural) (-RRB- -RRB-) (NNS languages)))))))))) (. .))) </parse>
"""

for line in parse:
    line_elem = line.text.split()
    for i, elem in enumerate(line_elem):
        if "(NP" in elem:  # (NPが現れたら括弧のカウント開始
            key = i
            while(1):
                if len(line_elem) <= key:
                    break
                cnt = cnt + line_elem[key].count("(")   # "("1つにつきcntを+1
                cnt = cnt - line_elem[key].count(")")   # ")"1つにつきcntを-1
                np_list.append(line_elem[key])
                key += 1
                if cnt == 0:    # cnt = 0になったら一つの名詞句のかたまり完成　-> ["(NP", "(JJ", "Natural)", "(NN", "language)", "(NN", "processing))"]
                    break

            if "." in np_list[-1] or "," in np_list[-1]:    # 名詞句の最後の"."や","を削除
                np_list.remove(np_list[-1])

            for word in np_list:    # word = ["(NP", "(JJ", "Natural)", "(NN", "language)", "(NN", "processing))"]
                if not word.startswith("("):
                    if "-LRB-" in word:
                        word = re.sub("-LRB-", "(", word)
                    if "-RRB-" in word:
                        word = re.sub("-RRB-", ")", word)
                    word = word.strip(")")
                    if word == "":
                        word = ")"
                    result_list.append(word)
            print " ".join(result_list)
            result_list = list()
            np_list = list()
            cnt = 0

"""
$ python mk59.py < nlp.txt.out
Natural language processing
Wikipedia
the free encyclopedia Natural language processing ( NLP )
the free encyclopedia Natural language processing
NLP
a field of computer science , artificial intelligence , and linguistics concerned with the interactions between computers and human ( natural ) languages
a field of computer science
a field
computer science ,
artificial intelligence
linguistics concerned with the interactions between computers and human ( natural ) languages
linguistics
the interactions between computers and human ( natural ) languages
the interactions
computers and human ( natural ) languages
computers
human ( natural ) languages
...
"""
