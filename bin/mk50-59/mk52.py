# coding=utf-8

"""
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
"""

from nltk import stem
import sys

stemmer = stem.PorterStemmer()
f = sys.stdin
for word in f:
    print word.strip() + "\t" + stemmer.stem(word.strip())

"""
Natural Natur
language        languag
processing      process
NLP     NLP
is      is
a       a
field   field
of      of
computer        comput
science scienc
artificial      artifici
intelligence    intellig
and     and
linguistics     linguist
concerned       concern
with    with
the     the
interactions    interact
between between
computers       comput
and     and
human   human
natural natur
languages       languag

As      As
such    such
NLP     NLP
is      is
related relat
...
"""
