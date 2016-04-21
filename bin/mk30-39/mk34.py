# coding=utf-8

"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

import mk30

data = mk30.load_morph()
for num, line in enumerate(data):
    if line["surface"] == "の" and data[num - 1]["pos"] == "名詞" and data[num + 1]["pos"] == "名詞":
        print data[num - 1]["surface"] + line["surface"] + data[num + 1]["surface"]

"""
スライディングウィンドウ
"""

"""
$ python mk34.py
彼の掌
掌の上
書生の顔
はずの顔
顔の真中
穴の中
書生の掌
掌の裏
何の事
肝心の母親
藁の上
笹原の中
池の前
池の上
一樹の蔭
垣根の穴
隣家の三
時の通路
一刻の猶予
...
"""
