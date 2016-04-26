# coding=utf-8

"""
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

import pydot
import sys, re
import mk41

phrase_dst_ls = list()
sentence_ls = list()
all_ls = list()
pattern = re.compile(r"。|、|　")

data = mk41.load_cabocha(sys.stdin)[7]
for line in data:
    phrase_dst_ls.append(pattern.sub("", line.phrase))  # 句読点等削除
    phrase_dst_ls.append(line.dst)
    sentence_ls.append(phrase_dst_ls)
    phrase_dst_ls = list()

dst_src_ls = list()
ls = list()
for index in sentence_ls:
    if index[1] == -1:
        break
    else:
        if index[0] == "":
            continue
        else:
            dst_src_ls.append(index[0])
            dst_src_ls.append(sentence_ls[index[1]][0])
            ls.append(tuple(dst_src_ls))
            dst_src_ls = list()

g=pydot.graph_from_edges(ls)
g.write_jpeg('dst_src_graph.jpg', prog='dot')

"""
$ python mk44.py < neko.txt.cabocha
http://www.cl.ecei.tohoku.ac.jp/~masakuri/nlp100/dst_src_graph
"""
