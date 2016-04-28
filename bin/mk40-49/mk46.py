# coding=utf-8

"""
46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

・項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
・述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
"""

import mk41
import sys, re

data = mk41.load_cabocha(sys.stdin)
pattern = re.compile(r"。|、|「|」|\*|　")   # mk45からの変更行
for sentence in data:
    for chunk in sentence:
        verb = ""
        dst_ls = list()
        kou_ls = list() # mk45からの追加行

        for morph in chunk.morphs:
            if morph.pos == "動詞":
                verb = morph.base
                break

        if verb != "" and len(chunk.srcs) > 0:
            for src_index in chunk.srcs:
                src_chunk = sentence[src_index]
                joshi = ""
                for morph in src_chunk.morphs:
                    if morph.pos == "助詞":
                        joshi = morph.base
                if joshi != "":
                    kou_ls.append(sentence[src_index].phrase)   # mk45からの追加行
                    dst_ls.append(joshi)
            if len(dst_ls) > 0:
                print pattern.sub("", verb + "\t" + " ".join(dst_ls) + "\t" + " ".join(kou_ls)) # mk45からの変更行

"""
$ python mk46.py < neko.txt.cabocha
生れる  で      どこで
つく    か が   生れたか 見当が
泣く    で      所で
する    て は   泣いて いた事だけは
始める  で      ここで
見る    は を   吾輩は ものを
聞く    で      あとで
捕える  を      我々を
煮る    て      捕えて
食う    て      煮て
思う    から    なかったから
載せる  に      掌に
持ち上げる      て と   載せられて スーと
ある    が      感じが
落ちつく        で      上で
...
"""
