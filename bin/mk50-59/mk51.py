# coding=utf-8

"""
51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
"""

import sys, re

f = sys.stdin
remove_pattern = re.compile(r"[.,\";:)(]")
for line in f:
    word_ls = line.split()
    for word in word_ls:
        print re.sub(remove_pattern, "", word)
    print "\n",

"""
$ python mk51.py < result50.txt > result51.txt
$ less result51.txt
Natural
language
processing
NLP
is
a
field
of
computer
science
artificial
intelligence
and
linguistics
concerned
with
the
interactions
between
computers
and
human
natural
languages

As
such
NLP
is
...
"""
