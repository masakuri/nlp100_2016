# coding=utf-8

"""
49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．

・問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
・文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
また，係り受けパスの形状は，以下の2通りが考えられる．

・文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
・上記以外で，文節iと文節jjから構文木の根に至る経路上で共通の文節kkで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示
"""

"""
chunk = [morphs=[[surface, base, pos, pos1], ...], dst, srcs, phrase]
chunk = [[[我輩, 我輩, 名詞, 代名詞], [は, は, 助詞, 助詞]], 2, [0], 我輩は]
"""

import mk41
import sys, re
from itertools import combinations

def main():
    data = mk41.load_cabocha(sys.stdin)
    pattern = re.compile(r"。|、|「|」|\*|　")
    # noun_flag = 0
    path_ls = list()

    for sentence in data:
        for chunk in sentence:
            noun_flag = 0
            for morph in chunk.morphs:
                if morph.pos == "名詞":   # 文節chunkに名詞があるか
                    noun_flag = 1
                    break
            if noun_flag == 1:  # 名詞があったら
                all_path = list()
                all_path.append(chunk)    # 係り元のchunkをall_pathリストに追加
                # pass_ls.append(chunk.phrase)
                dst_path = chunk.dst
                while(dst_path != -1):  # 係り先がある限り
                    dst_chunk = sentence[dst_path]
                    all_path.append(dst_chunk)  # 係り先のchunkをall_pathリストに追加
                    dst_path = dst_chunk.dst
                path_ls.append(all_path)

    list_of_nodes = [{"chunk": l[0], "path": l} for l in path_ls]
    for node_i, node_j in combinations(list_of_nodes, 2):
        if node_j["chunk"] in node_i["path"]:   # node_iから構文木の根までのパスにnode_jが存在する場合
            index_j_in_i = node_i["path"].index(node_j["chunk"])
            path_ij = node_i["path"][0:index_j_in_i + 1]
            path_ij_surfaces = [chunk.phrase for chunk in path_ij]
            path_ij_surfaces[0] = replace_noun_phrase_in_chunk(path_ij[0], "X")
            path_ij_surfaces[-1] = "Y"

            print " -> ".join(path_ij_surfaces)

        else:   # node_iと文節node_jから構文木の根までのパス上で共通のnode_kで交わる場合
            node_k_chunk = None
            h = -1
            while(node_i["path"][h] == node_j["path"][h]):
                node_k_chunk = node_i["path"][h]
                h = h - 1

            if node_k_chunk != None:
                # node_iからnode_kまでのパスを取り出す
                index_k_in_i = node_i["path"].index(node_k_chunk)
                path_ik = node_i["path"][0:index_k_in_i]
                path_ik_surfaces = [re.sub(pattern, "", chunk.phrase) for chunk in path_ik]
                path_ik_surfaces[0] = replace_noun_phrase_in_chunk(path_ik[0], "X")
                
                # node_jからnode_kまでのパスを取り出す
                index_k_in_j = node_j["path"].index(node_k_chunk)
                path_jk = node_j["path"][0:index_k_in_j]
                path_jk_surfaces = [re.sub(pattern, "", chunk.phrase) for chunk in path_jk]
                path_jk_surfaces[0] = replace_noun_phrase_in_chunk(path_jk[0], "Y")

                print " -> ".join(path_ik_surfaces) \
                    + " | " + " -> ".join(path_jk_surfaces) \
                    + " | " + re.sub(pattern, "", node_k_chunk.phrase)

# chunk内の名詞句をnew_stringに置換して文字列として返す
def replace_noun_phrase_in_chunk(chunk, new_string):
    phrase_x = ""
    prev_is_noun = False
    for morph in chunk.morphs:
        if morph.pos == "名詞":
            phrase_x += morph.surface
            prev_is_noun = True
        elif morph.pos != "名詞" and prev_is_noun:
            break
    return chunk.phrase.replace(phrase_x, new_string)

if __name__ == '__main__':
    main()

"""
$ python mk49.py < neko.txt.cabocha
Xは -> Y
　Xで -> 生れたか | Yが | つかぬ
Xでも -> 薄暗い -> Y
Xでも -> 薄暗い -> 所で | Y | 泣いて
Xでも -> 薄暗い -> 所で -> 泣いて | Yだけは | 記憶している
Xでも -> 薄暗い -> 所で -> 泣いて -> Y
Xで | Y | 泣いて
Xで -> 泣いて | Yだけは | 記憶している
Xで -> 泣いて -> Y
X -> 泣いて | Yだけは | 記憶している
X -> 泣いて -> Y
Xだけは -> Y
Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
...
"""
