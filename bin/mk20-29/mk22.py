# coding=utf-8

import mk20, re

pattern = re.compile(r"\[\[Category:(?P<category>.*)\]\]")
for line in mk20.uk().split("\n"):
    if "Category" in line:
        p = re.search(pattern, line)
        print p.group("category").rstrip("|*")

"""
> python mk22.py
イギリス
英連邦王国
G8加盟国
欧州連合加盟国
海洋国家
君主国
島国|くれいとふりてん
1801年に設立された州・地域
"""
