# coding=utf-8

"""
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""

import sys, re
import mk41

def dst_srcs(f):
    data = mk41.load_cabocha(f)
    dst_phrase_src_ls = list()
    sentense_ls = list()
    all_ls = list()
    pattern = re.compile(r"。|、|\　")

    # 0:吾輩は -> 5 を [0, 我輩は, 5]とするリスト作成
    for sentense in data:
        for line in sentense:
            dst_phrase_src_ls.append(line.dst)
            dst_phrase_src_ls.append(pattern.sub("", line.phrase))  # 句読点等削除
            dst_phrase_src_ls.append(line.srcs)
            sentense_ls.append(dst_phrase_src_ls)
            dst_phrase_src_ls = list()
        all_ls.append(sentense_ls)
        sentense_ls = list()

    return all_ls

if __name__ == '__main__':
    lst = dst_srcs(sys.stdin)
    for sentense in lst:
        for index in sentense:
            if index[2] == "-1":
                break
            else:
                if index[1] == "":
                    continue
                else:
                    print index[1]+ "\t" + sentense[int(index[2])][1]

"""
$ python mk42.py < neko.txt.cabocha
吾輩は  猫である
名前は  無い
まだ    無い
どこで  生れたか
生れたか        つかぬ
とんと  つかぬ
見当が  つかぬ
何でも  薄暗い
薄暗い  所で
じめじめした    所で
所で    泣いて
ニャーニャー    泣いて
泣いて  記憶している
いた事だけは    記憶している
吾輩は  見た
ここで  始めて
始めて  人間という
人間という      ものを
ものを  見た
...
"""
