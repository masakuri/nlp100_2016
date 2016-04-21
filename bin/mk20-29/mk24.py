# coding=utf-8

import mk20

for line in mk20.uk().split("\n"):
    if "ファイル" in line or "File" in line:
        print line.split(":")[1].split("|")[0]

"""
> python mk24.py
Royal Coat of Arms of the United Kingdom.svg
Battle of Waterloo 1815.PNG
The British Empire.png
Uk topo en.jpg
BenNevis2005.jpg
...
"""
