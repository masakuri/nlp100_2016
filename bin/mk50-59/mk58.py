# coding=utf-8

"""
58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．

・述語: nsubj関係とdobj関係の子（dependant）を持つ単語
・主語: 述語からnsubj関係にある子（dependent）
・目的語: 述語からdobj関係にある子（dependent）
"""

from xml.etree.ElementTree import *
import sys

tree = parse(sys.stdin)
elem = tree.getroot()
collapsed_dependencies = elem.findall(".//dependencies[@type='collapsed-dependencies']")
nsub_dob_ls = list()
tuple_list = list()

"""
<dep type="nsubj">
  <governor idx="13">enabling</governor>
  <dependent idx="8">understanding</dependent>
</dep>

<dep type="dobj">
  <governor idx="13">enabling</governor>
  <dependent idx="14">computers</dependent>
</dep>
"""
# [[nsubj, enabling, 13, understanding, 8], [dobj, enabling, 13, computers, 14]]みたいなリスト作成
for dependency in collapsed_dependencies:
    for dep in dependency:
        if dep.get("type") in ["nsubj", "dobj"]:
            nsub_dob_ls.append([dep.get("type"), dep.find("governor").text, dep.find("governor").attrib["idx"], \
            dep.find("dependent").text, dep.find("dependent").attrib["idx"]])
    if len(nsub_dob_ls) > 0:
        tuple_list.append(nsub_dob_ls)
    nsub_dob_ls = list()

# 同一文中で、nsubjとdobjのidx番号が一致するものを探索
for dependence in tuple_list:
    if len(dependence) > 1:
        for nsubj in dependence:
            if nsubj[0] == "nsubj":
                subj = nsubj[2]  # subj = 13
                for dobj in dependence:
                    if dobj[0] == "dobj" and dobj[2] == subj:
                        print nsubj[3] + "\t" + nsubj[1] + "\t" + dobj[3]

"""
$ python mk58.py < nlp.txt.out
understanding   enabling        computers
others  involve generation
Turing  published       article
experiment      involved        translation
ELIZA   provided        interaction
patient exceeded        base
ELIZA   provide response
which   structured      information
underpinnings   discouraged     sort
that    underlies       approach
Some    produced        systems
which   make    decisions
systems rely    which
that    contains        errors
implementations involved        coding
algorithms      take    set
Some    produced        systems
which   make    decisions
models  have    advantage
they    express certainty
Systems have    advantages
Automatic       make    use
that    make    decisions
"""
