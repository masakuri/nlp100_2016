# coding=utf-8

col0 = [line.split()[0] for line in open("../../data/hightemp.txt")]
col0_count = {pref: col0.count(pref) for pref in col0}

for pref, freq in sorted(col0_count.iteritems(), key=lambda x: x[1], reverse=True):
    print pref, freq

"""
cut -f 1 ../../data/hightemp.txt | sort | uniq -c | sort -r
"""
