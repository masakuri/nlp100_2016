# coding=utf-8

"""
83. 単語／文脈の頻度の計測
82の出力を利用し，以下の出現分布，および定数を求めよ．

f(t,c): 単語tと文脈語cの共起回数
f(t,∗): 単語tの出現回数
f(∗,c): 文脈語cの出現回数
N: 単語と文脈語のペアの総出現回数
"""
from collections import defaultdict, Counter
import sys
from tqdm import tqdm

data = sys.stdin
f_tc = defaultdict(int)
f_t = defaultdict(int)
f_c = defaultdict(int)
N = 0

for line in tqdm(data):   # 各単語文脈語に対して
    N += 1
    word_pair = line.strip("\n").split(" ") # [単語, 文脈語]
    word = word_pair[0]
    context_word = word_pair[1]
    f_tc[line.rstrip("\n")] += 1    # 単語tと文脈語cの共起回数
    f_t[word] += 1  # 単語tの出現回数
    f_c[context_word] += 1  # 文脈語cの出現回数

# 1ファイルに全て出力
print "*****(f_tc)*****"
for k, v in f_tc.iteritems():
    print k, v
print "*****(f_t)*****"
for k, v in f_t.iteritems():
     print k, v
print "*****(f_c)*****"
for k, v in f_c.iteritems():
    print k, v
print "*****N*****"
print N

"""
$ time zcat enwiki_context.txt.gz| python mk83.py | gzip > enwiki_wordfreq.gz
zcat enwiki_wordfreq.gz  4.69s user 0.24s system 13% cpu 35.498 total
python mk84.py  90.81s user 7.46s system 91% cpu 1:47.18 total
gzip > enwiki_wcarray.txt.gz  0.88s user 0.02s system 0% cpu 1:47.18 total
メモリ：1.5Gくらい
$ zcat enwiki_wordfreq.gz| less
*****(f_tc)*****
d long 1
Manson Arctic 1
Biblical date 2
Ya composed 1
1877-8 from 1
shares zip 1
be constructed 82
...
*****(f_t)*****
biennials 14
unsupportable 2
Goto.com 12
others.’ 2
470 nm 2
Laiharaoba 18
woods 980
...
*****(f_c)*****
biennials 16
unsupportable 3
Goto.com 12
others.’ 6
470 nm 7
Laiharaoba 15
woods 943
...
*****N*****
68005354
"""

"""
$ time zcat enwiki_context10.txt.gz| python mk83.py | gzip > enwiki_wordfreq10.gz（martini01）
zcat enwiki_context10.txt.gz  58.84s user 5.71s system 4% cpu 25:39.03 total
python mk83.py  1707.90s user 39.79s system 97% cpu 29:53.83 total
gzip > enwiki_wordfreq10.gz  157.94s user 1.37s system 8% cpu 29:53.83 total
"""
# 1/10
