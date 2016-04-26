# coding=utf-8

"""
45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
ただし，出力は以下の仕様を満たすようにせよ．

・動詞を含む文節において，最左の動詞の基本形を述語とする
・述語に係る助詞を格とする
・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
(中略)
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

・コーパス中で頻出する述語と格パターンの組み合わせ
・「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
"""

"""
chunk = [morphs=[[surface, base, pos, pos1], ...], dst, srcs, phrase]
chunk = [[[我輩, 我輩, 名詞, 代名詞], [は, は, 助詞, 助詞]], 2, [0], 我輩は]
"""

import mk41
import sys, re

data = mk41.load_cabocha(sys.stdin)
pattern = re.compile(r"。|、|「|」|\*")
for sentence in data:
    for chunk in sentence:
        verb = ""
        dst_ls = list()

        for morph in chunk.morphs:
            if morph.pos == "動詞":
                verb = morph.base
                break

        if verb != "" and len(chunk.srcs) > 0:
            for src_index in chunk.srcs:
                src_chunk = sentence[int(src_index)]
                joshi = None
                for morph in src_chunk.morphs:
                    if morph.pos == "助詞":
                        joshi = morph.base
                if joshi:
                    dst_ls.append(morph.base)
            if len(dst_ls) > 0:
                sortedlist = sorted(dst_ls)
                print pattern.sub("", verb + "\t" + " ".join(sortedlist))

"""
$ python mk45.py < neko.txt.cabocha > result45.txt
$ less result45.txt
生れる  で
つく    か が
泣く    で
する    て は
始める  で
見る    は を
聞く    で
捕える  を
煮る    て
食う    て
思う    から
載せる  に
持ち上げる      て と
ある    が
落ちつく        で
...

$ cat result45.txt | sort | uniq -c | sort -rn | less
    704 云う    と
    450 する    を
    333 思う    と
    202 ある    が
    199 なる    に
    186 する    に
    175 見る    て
    157 する    と
    116 する    が
    109 する    に を
     97 見える  と
     97 見る    を
     ...

$ cat result45.txt | sort | uniq -c | sort -rn | grep -w する | less
    450 する    を
    186 する    に
    157 する    と
    116 する    が
    109 する    に を
     83 する    は
     75 する     を
     60 する    て を
     58 する    も
     55 する    が を
     52 する    て
     ...

$ cat result45.txt | sort | uniq -c | sort -rn | grep -w 見る | less
    175 見る    て
     97 見る    を
     28 見る     て
     20 見る    から
     17 見る    と
     13 見る    て は
     12 見る    で
     11 見る    て て
     10 見る    て を
     ...

$ cat result45.txt | sort | uniq -c | sort -rn | grep -w 与える | less
      4 与える  に を
      2 与える   に を
      1 与える  か として
      1 与える  て に は を
      1 与える  て と は を
      1 与える  は は も
      1 与える  て に を
      1 与える  も を
      1 与える  ば を
      1 与える   に に は を
      1 与える   は を
      1 与える   を
      1 与える    て と に は を
      1 与える    は を
"""
