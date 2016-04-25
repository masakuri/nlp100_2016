# coding=utf-8

"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import mk30
from collections import defaultdict

def word_count():
    data = mk30.load_morph()
    word_counter = defaultdict(int)

    for line in data:
        word_counter[line["base"]] += 1

    return word_counter

if __name__ == '__main__':
    cnt = word_count()
    for freq, word in sorted(cnt.iteritems(), key = lambda x: x[1], reverse = True):
        print freq, word

"""
$ python mk36.py
の 9194
。 7486
て 6848
、 6772
は 6420
に 6243
を 6071
だ 5975
と 5508
が 5337
た 4267
する 3657
「 3231
」 3225
ない 3052
も 2479
ある 2320
...
"""
