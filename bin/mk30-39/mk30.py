# coding=utf-8

"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

"""
$ mecab ../../data/neko.txt > neko.txt.mecab
"""

def load_morph():
    sentence_morph_ls = list()
    morph_dic = dict()
    with open("neko.txt.mecab", "r") as f:
        for line in f:
            if "EOS" in line:
                continue
            else:
                ls = line.split()
                mecab_ls = ls[1].split(",")
                morph_dic["surface"] = ls[0]
                morph_dic["base"] = mecab_ls[6]
                morph_dic["pos"] = mecab_ls[0]
                morph_dic["pos1"] = mecab_ls[1]
                sentence_morph_ls.append(morph_dic)
                morph_dic = dict()
                text_morph_ls = list()
        return sentence_morph_ls

if __name__ == '__main__':
    print lead_morph()

"""
・1文をリストにすること！
・groupby
・(**hoge)s
"""
