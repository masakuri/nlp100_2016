# coding=utf-8

"""
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
・述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
・述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
（中略）
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

・コーパス中で頻出する述語（サ変接続名詞+を+動詞）
・コーパス中で頻出する述語と助詞パターン
"""

"""
chunk = [morphs=[[surface, base, pos, pos1], ...], dst, srcs, phrase]
chunk = [[[我輩, 我輩, 名詞, 代名詞], [は, は, 助詞, 助詞]], 2, [0], 我輩は]
"""

import mk41
import sys, re

data = mk41.load_cabocha(sys.stdin)
pattern = re.compile(r"。|、|「|」|\*|　")
for sentence in data:
    for chunk in sentence:
        verb = ""
        dst_ls = list()
        kou_ls = list()

        for morph in chunk.morphs:
            if morph.pos == "動詞":
                verb = morph.base
                break

        if verb != "" and len(chunk.srcs) > 0:
            sahen_wo = ""
            for src_index in chunk.srcs:
                src_chunk = sentence[src_index]
                if len(src_chunk.morphs) > 1 and src_chunk.morphs[0].pos1 == "サ変接続" and src_chunk.morphs[1].base == "を":
                    sahen_wo = src_chunk.phrase
                    continue
                joshi = ""
                for morph in src_chunk.morphs:
                    if morph.pos == "助詞":
                        joshi = morph.base
                if joshi != "":
                    kou_ls.append(sentence[src_index].phrase)
                    dst_ls.append(joshi)
            if len(dst_ls) > 0 and sahen_wo != "":
                print pattern.sub("", sahen_wo + verb + "\t" + " ".join(dst_ls) + "\t" + " ".join(kou_ls))

"""
$ python mk47.py < neko.txt.cabocha > result47.txt
$ less result47.txt
決心をする      と      こうと
返報をする      んで    偸んで
昼寝をする      が      彼が
迫害を加える    て      追い廻して
投書をする      て へ   やって ほととぎすへ
話をする        に      時に
昼寝をする      て      出て
欠伸をする      から て て      なったから して 押し出して
報道をする      に      耳に
御馳走を食う    と      見ると
雑談をする      は ながら       黒は 寝転びながら
呼吸を飲み込む  から    なってから
思案を定める    は と   吾輩は 若くはないと
御馳走をあるく  て って なって 猟って
放蕩をする      が      ものだから○○が
...

$ cat result47.txt | cut -f1 | sort | uniq -c | sort -rn | less
     25 返事をする
     19 挨拶をする
     11 話をする
      8 質問をする
      7 喧嘩をする
      6 真似をする
      5 質問をかける
      5 相談をする
      5 昼寝をする
      4 休養を要する
      4 演説をする
      4 注意をする
      4 欠伸をする
      3 落着を告げる
      ...

$ cat result47.txt | cut -f1,2 | sort | uniq -c | sort -rn | less
      6 返事をする      と
      4 挨拶をする      から
      4 挨拶をする      と
      3 質問をかける    と は
      3 返事をする      は と
      3 喧嘩をする      と
      2 同情を表する    と は て
      2 休養を要する    は
      2 挨拶をする      と も
      2 議論をする      て
      2 講義をする      で
      2 覚悟をする      と
      2 挨拶をする      で
      2 安心を得る      が
      ...
"""
