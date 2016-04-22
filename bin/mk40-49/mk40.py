# coding=utf-8

"""
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""

"""
cabocha -f1 ../../data/neko.txt > neko.txt.cabocha
"""

import sys

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return self.surface + "\t" + self.base + "," + self.pos + "," + self.pos1

def load_cabocha(f):
    result_morph = []
    result_sentence = []
    for line in f:
        if line.startswith("*"):
            continue
        elif line == "EOS\n":
            result_sentence.append(result_morph)
            result_morph = []
            continue
        else:
            morph_split = line.split()
            morph_list = morph_split[1].split(",")
            surface = morph_split[0]
            base = morph_list[6]
            pos = morph_list[0]
            pos1 = morph_list[1]
            result_morph.append(Morph(surface, base, pos, pos1))
    return result_sentence

def print_list(li):
    for item in li:
        print str(item)

if __name__ == '__main__':
    print_list(load_cabocha(sys.stdin)[2])

"""
$ python mk40.py < neko.txt.cabocha
[　,　,記号,空白]
[吾輩,吾輩,名詞,代名詞]
[は,は,助詞,係助詞]
[猫,猫,名詞,一般]
[で,だ,助動詞,*]
[ある,ある,助動詞,*]
[。,。,記号,句点]
"""
