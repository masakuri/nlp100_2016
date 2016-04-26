# coding=utf-8

"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""

"""
chunk = [morphs=[[surface, base, pos, pos1], ...], dst, srcs, phrase]
chunk = [[[我輩, 我輩, 名詞, 代名詞], [は, は, 助詞, 助詞]], 2, [0], 我輩は]
"""

import sys, re
import mk41

data = mk41.load_cabocha(sys.stdin)
pattern = re.compile(r"。|、|　")

for sentence in data:
    for chunk in sentence:
        for morpheme in chunk.morphs:
            if morpheme.pos == "名詞" and chunk.dst != -1:
                noun_src = pattern.sub("",chunk.phrase) # 句読点等削除
                for is_verb_morphs in sentence[chunk.dst].morphs:
                    if is_verb_morphs.pos == "動詞":
                        verb_dst = pattern.sub("", sentence[chunk.dst].phrase)  # 句読点等削除
                        print noun_src + "\t" + verb_dst
                        break
                break


"""
$ python mk43.py < neko.txt.cabocha
どこで  生れたか
見当が  つかぬ
所で    泣いて
ニャーニャー    泣いて
いた事だけは    記憶している
吾輩は  見た
ここで  始めて
ものを  見た
あとで  聞くと
我々を  捕えて
掌に    載せられて
スーと  持ち上げられた
時      フワフワした
感じが  あったばかりである
...
"""
