# coding=utf-8

"""
70. データの入手・整形
文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．
"""

import random

with open ("../../data/rt-polaritydata/rt-polarity.neg") as neg, open ("../../data/rt-polaritydata/rt-polarity.pos") as pos:
    sentiment_ls = list()
    for neg_line in neg:
        sentiment_ls.append("-1 " + neg_line)
    for pos_line in pos:
        sentiment_ls.append("+1 " + pos_line)
    random.shuffle(sentiment_ls)
    for line in sentiment_ls:
        print line,

"""
$ python mk70.py > sentiment.txt
$ less sentiment.txt
-1 who are 'they' ? well , they're 'they' . they're the unnamed , easily substitutable forces that serve as whatever terror the heroes of horror movies try to avoid . they exist for hushed lines like " they're back ! " , " they're out there ! " and " they're coming ! "
-1 sets up a nice concept for its fiftysomething leading ladies , but fails loudly in execution .
-1 his comedy premises are often hackneyed or just plain crude , calculated to provoke shocked laughter , without following up on a deeper level .
+1 'divertida , enternecedora , universal y profundamente sincera , es una de las mejores comedias rom<E1>nticas en mucho tiempo . una verdadera delicia . '
+1 the script's snazzy dialogue establishes a realistic atmosphere that involves us in the unfolding crisis , but the lazy plotting ensures that little of our emotional investment pays off .
-1 might be one of those vanity projects in which a renowned filmmaker attempts to show off his talent by surrounding himself with untalented people .
...
"""

"""
cut -d " " -f1 sentiment.txt | sort | uniq -c
   5331 +1
   5331 -1
"""
