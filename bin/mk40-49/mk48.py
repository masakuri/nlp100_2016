# coding=utf-8

"""
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

・各文節は（表層形の）形態素列で表現する
・パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
"""

"""
chunk = [morphs=[[surface, base, pos, pos1], ...], dst, srcs, phrase]
chunk = [[[我輩, 我輩, 名詞, 代名詞], [は, は, 助詞, 助詞]], 2, [0], 我輩は]
"""

import mk41
import sys, re

data = mk41.load_cabocha(sys.stdin)
pattern = re.compile(r"。|、|「|」|\*|　")
pass_ls = list()
noun_flag = 0
for sentence in data:
    for chunk in sentence:
        for morph in chunk.morphs:
            if morph.pos == "名詞":
                noun_flag = 1
                break
        if noun_flag == 1:
            pass_ls.append(chunk.phrase)
            dst_pass = chunk.dst
            while(dst_pass != -1):
                pass_ls.append(sentence[dst_pass].phrase)
                dst_pass = sentence[dst_pass].dst
            if len(pass_ls) > 1:
                print pattern.sub("", " -> ".join(pass_ls).rstrip(" -> "))
            noun_flag = 0
            pass_ls = list()

"""
$ python mk48.py < neko.txt.cabocha
吾輩は -> 猫である
名前は -> 無い
どこで -> 生れたか -> つかぬ
見当が -> つかぬ
何でも -> 薄暗い -> 所で -> 泣いて -> 記憶している
所で -> 泣いて -> 記憶している
ニャーニャー -> 泣いて -> 記憶している
いた事だけは -> 記憶している
吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
あとで -> 聞くと -> 種族であったそうだ
それは -> 種族であったそうだ
書生という -> 人間中で -> 種族であったそうだ
人間中で -> 種族であったそうだ
一番 -> 獰悪な -> 種族であったそうだ
獰悪な -> 種族であったそうだ
...
"""
