# coding=utf-8

"""
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import sys
from collections import defaultdict

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
        return self.phrase + " -> " + str(self.dst)

def load_cabocha(f):
    list_of_sentence = []
    list_of_morphs = []
    list_of_chunk = []
    src_tmp = None
    dst_tmp = None
    dst_srcs_dict = defaultdict(list)
    for line in f:
        # *行処理
        if line.startswith("*"):
            if len(list_of_morphs) > 0: # 最初の行か否か判定（0の場合最初の行）
                list_of_srcs = dst_srcs_dict[src_tmp]
                list_of_chunk.append(Chunk(list_of_morphs, dst_tmp, list_of_srcs))
                list_of_morphs = []
            src_tmp = int(line.rstrip().split()[1])
            dst_tmp = int(line.rstrip().split()[2].strip("D"))
            dst_srcs_dict[dst_tmp].append(src_tmp)
        # 形態素の行処理
        elif "\t" in line:
            surface, rest = line.rstrip().split("\t")
            list_of_rest = rest.split(",")
            base = list_of_rest[6]
            pos = list_of_rest[0]
            pos1 = list_of_rest[1]
            list_of_morphs.append(Morph(surface, base, pos, pos1))
        # EOS行処理
        elif "EOS" in line:
            list_of_srcs = dst_srcs_dict[src_tmp]
            list_of_chunk.append(Chunk(list_of_morphs, dst_tmp, list_of_srcs))
            list_of_sentence.append(list_of_chunk)
            list_of_morphs = []
            list_of_chunk = []
            dst_srcs_dict = defaultdict(list)

    return list_of_sentence

def print_list(lst):
    for index, item in enumerate(lst):
        print str(index) + ":" + str(item)

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
