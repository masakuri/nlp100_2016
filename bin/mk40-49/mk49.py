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
                if morph.pos == "名詞":
                    noun_flag = 1
                    break
            if noun_flag == 1:
                a_path = list()
                a_path.append(chunk)
                # pass_ls.append(chunk.phrase)
                dst_path = chunk.dst
                while(dst_path != -1):
                    dst_chunk = sentence[dst_path]
                    a_path.append(dst_chunk)
                    dst_path = dst_chunk.dst
                path_ls.append(a_path)

    list_of_nodes = [{"chunk": l[0], "path": l} for l in path_ls]
    for node_i, node_j in combinations(list_of_nodes, 2):
        if node_j["chunk"] in node_i["path"]:
            index_j_in_i = node_i["path"].index(node_j["chunk"])
            path_ij = node_i["path"][0:index_j_in_i + 1]
            path_ij_surfaces = [chunk.phrase for chunk in path_ij]
            path_ij_surfaces[0] = replace_noun_phrase_in_chunk(path_ij[0], "X")
            path_ij_surfaces[-1] = "Y"

            print " -> ".join(path_ij_surfaces)

        else:
            """
            ?????
            """

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
