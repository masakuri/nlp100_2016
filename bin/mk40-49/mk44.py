# coding=utf-8

import pydot
import sys, re
import mk41

dst_phrase_src_ls = list()
sentense_ls = list()
all_ls = list()
pattern = re.compile(r"。|、|\　")

data = mk41.load_cabocha(sys.stdin)[7]
for line in data:
    dst_phrase_src_ls.append(line.dst)
    dst_phrase_src_ls.append(pattern.sub("", line.phrase))  # 句読点等削除
    dst_phrase_src_ls.append(line.srcs)
    sentense_ls.append(dst_phrase_src_ls)
    dst_phrase_src_ls = list()

dst_src_ls = list()
ls = list()
for index in sentense_ls:
    if index[2] == "-1":
        break
    else:
        if index[1] == "":
            continue
        else:
            dst_src_ls.append(index[1])
            dst_src_ls.append(sentense_ls[int(index[2])][1])
            ls.append(tuple(dst_src_ls))
            dst_src_ls = list()

g=pydot.graph_from_edges(ls)
g.write_jpeg('dst_src_graph.jpg', prog='dot')

"""
http://www.cl.ecei.tohoku.ac.jp/~masakuri/nlp100/dst_src_graph
"""
