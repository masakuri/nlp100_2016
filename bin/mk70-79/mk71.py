# coding=utf-8

"""
71. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．
"""

"""
ストップワードは以下から拝借
http://www.textfixer.com/resources/common-english-words.txt
"""

def is_stop_word(word, stop_list):
    return word in stop_list

def main(text, stop_list):
    word_ls = text.split()
    for word in word_ls:
        print "{}\t{}".format(word, is_stop_word(word, stop_list))

if __name__ == '__main__':
    with open("stop_word.txt") as f:
        stop_list = f.read().strip().split(",")
        main("it's so laddish and juvenile , only teenage boys could possibly find it funny .", stop_list)
        print "********************"
        main("if you sometimes like to go to the movies to have fun , wasabi is a good place to start .", stop_list)

"""
$ python mk71.py
it's	False
so	True
laddish	False
and	True
juvenile	False
,	False
only	True
teenage	False
boys	False
could	True
possibly	False
find	False
it	True
funny	False
.	False
if	True
you	True
sometimes	False
like	True
to	True
go	False
to	True
the	True
movies	False
to	True
have	True
fun	False
,	False
wasabi	False
is	True
a	True
good	False
place	False
to	True
start	False
.	False
"""
