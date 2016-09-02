# coding=utf-8

"""
71. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．
"""

"""
ストップワードは以下から拝借
http://www.textfixer.com/resources/common-english-words.txt
"""

import sys

def is_stop_word(word, stop_list):
    return word in stop_list

if __name__ == '__main__':
    with open("stop_word.txt") as f:
        stop_list = f.read().strip().split(",")
        print is_stop_word(sys.argv[1], stop_list)

"""
$ python mk71.py can
True
"""
