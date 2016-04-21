# coding=utf-8

"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import mk30
from collections import Counter
from collections import defaultdict

def word_count():
    data = mk30.load_morph()

    """
    word_ls = list()
    for line in data:
        word_ls.append(line["surface"])
    word_counter = Counter(word_ls)
    for word, cnt in word_counter.most_common():
        print word, cnt
    """

    word_counter = defaultdict(int)
    for line in data:
        word_counter[line["surface"]] += 1

    return word_counter

if __name__ == '__main__':
    cnt = word_count()
    for freq, word in sorted(cnt.iteritems(), key = lambda x: x[1], reverse = True):
        print freq, word

"""
$ python mk36.py
の 9194
。 7486
て 6868
、 6772
は 6420
に 6243
を 6071
と 5508
が 5337
た 3988
で 3806
「 3231
」 3225
も 2479
ない 2390
だ 2363
し 2322
から 2032
ある 1728
な 1613
ん 1568
か 1530
いる 1249
...
"""
