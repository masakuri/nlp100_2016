# coding=utf-8

"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""

import sys
import mk42
import MeCab

data = mk42.dst_srcs(sys.stdin)
m = MeCab.Tagger()
for sentense in data:
    for index in sentense:
        if index[2] == "-1":
            break
        else:
            if index[1] == "":
                continue
            else:
                if m.parse(index[1]).split()[1].split(",")[0] == "名詞" and m.parse(sentense[int(index[2])][1]).split()[1].split(",")[0] == "動詞":
                    print index[1]+ "\t" + sentense[int(index[2])][1]

"""
import sys, re
import mk41

data = mk41.load_cabocha(sys.stdin)
i = 0
for sentense in data:
    for chunk in sentense:
        for morpheme in chunk.morphs:
            print morpheme.surface
            # if morpheme.pos == "名詞" and i == 0:
            #     print morpheme.surface
            #     i += 1
            # elif morpheme.pos == "動詞" and i == 1:
            #     print morpheme.surface
            #     i = 0
        print "*****"
"""

"""
$ python mk43.py < neko.txt.cabocha
どこで  生れたか
見当が  つかぬ
所で    泣いて
ニャーニャー    泣いて
吾輩は  見た
ここで  始めて
ものを  見た
あとで  聞くと
我々を  捕えて
掌に    載せられて
...
"""
