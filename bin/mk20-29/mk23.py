# coding=utf-8

import mk20, re

pattern = re.compile(r"==+.+==+")
for line in mk20.uk().split("\n"):
    p = re.search(pattern, line)
    if p:
        level = p.group().rstrip("=").count("=") - 1
        print p.group().strip("=") + " : " + str(level)

"""
> python mk23.py
国名 : 1
歴史 : 1
地理 : 1
気候 : 2
政治 : 1
...
"""
