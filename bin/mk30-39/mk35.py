# coding=utf-8

"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

import mk30

data = mk30.load_morph()
noun_ls = list()
for num, line in enumerate(data):
    if line["pos"] == "名詞" and data[num + 1]["pos"] == "名詞":
        # noun = noun + line["surface"]
        noun_ls.append(line["surface"])
    elif line["pos"] == "名詞" and data[num + 1]["pos"] != "名詞":
        noun_ls.append(line["surface"])
        if len(noun_ls) >= 2:
            print "".join(noun_ls)
        noun_ls = list()

"""
itertoolsのgroupby便利！
"""

"""
$ python mk35.py
人間中
一番獰悪
時妙
一毛
その後猫
一度
ぷうぷうと煙
邸内
三毛
書生以外
...
大家アンドレア・デル・サルト
...
馬鹿野郎呼わり
...
同盟敬遠主義
...
美学者迷亭先生
...
鳥部教授歓迎会
...
"""
