# coding=utf-8

"""
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．
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

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.phrase = "".join([morph.surface for morph in self.morphs])
        self.dst = dst
        self.srcs = srcs

    def __str__(self):
        return self.dst + ":" + self.phrase + " -> " + self.srcs

def load_cabocha(f):
    result_morph = []
    result_morphs = []
    result_sentense = []
    result_chunk = []
    i = 0
    for line in f:
        # 最初の*行判定
        if line.startswith("*") and i == 0:
            dst = line.split()[1]
            srcs = line.split()[2].strip("D")
            continue
        # それ以降の*行判定
        elif line.startswith("*") and i != 0:
            result_chunk.append(Chunk(result_morph, dst, srcs))
            result_morph = []
            dst = line.split()[1]
            srcs = line.split()[2].strip("D")
            i += 1
            continue
        # 形態素の行判定
        elif "\t" in line:
            morph_split = line.split("\t")
            morph_list = morph_split[1].split(",")
            surface = morph_split[0]
            base = morph_list[6]
            pos = morph_list[0]
            pos1 = morph_list[1]
            result_morph.append(Morph(surface, base, pos, pos1))
            i += 1
        # EOS行判定
        elif line == "EOS\n":
            result_chunk.append(Chunk(result_morph, dst, srcs))
            result_morphs.append(result_chunk)
            result_morph = []
            result_chunk = []
            i = 0
            continue

    return result_morphs

def print_list(lst):
    for item in lst:
        print str(item)

if __name__ == '__main__':
    print_list(load_cabocha(sys.stdin)[7])

"""
$ python mk41.py < neko.txt.cabocha
0:吾輩は -> 5
1:ここで -> 2
2:始めて -> 3
3:人間という -> 4
4:ものを -> 5
5:見た。 -> -1
"""
