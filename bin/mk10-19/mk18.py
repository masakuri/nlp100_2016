# coding=utf-8

data = [line.split() for line in open("../../data/hightemp.txt")]

for line in sorted(data, key=lambda x: x[2],reverse=True):
    print "\t".join(line)


"""
sort -r -k 3 ../data/hightemp.txt
"""
