# coding=utf-8

"""
57. 係り受け解析
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

"""
<dependencies type="collapsed-dependencies">
  <dep type="root">
    <governor idx="0">ROOT</governor>
    <dependent idx="18">field</dependent>
  </dep>
  <dep type="amod">
    <governor idx="3">processing</governor>
    <dependent idx="1">Natural</dependent>
  </dep>
  ...
"""

import xml.etree.ElementTree as ET
import sys
import pydot

tree = ET.parse(sys.stdin)
elem = tree.getroot()
collapsed_dependencies = elem.findall(".//dependencies[@type='collapsed-dependencies']")
det_src_ls = list()
node_ls = list()
sentence_ls = list()

for dependency in collapsed_dependencies:
    for dep in dependency:
        if dep.find("dependent").text != "." and dep.find("dependent").text != ",":
            det_src_ls.append(dep.find("governor").text)
            det_src_ls.append(dep.find("dependent").text)
            node_ls.append(det_src_ls)
            det_src_ls = list()
    sentence_ls.append(node_ls)
    node_ls = list()

g=pydot.graph_from_edges(sentence_ls[11], directed=True)
g.write_jpeg('result57.jpg', prog='dot')

"""
$ python mk57.py < nlp.txt.out
http://www.cl.ecei.tohoku.ac.jp/~masakuri/nlp100/result57
一つのノードに2つ以上のエッジが入ってきている（おかしい）
"""
