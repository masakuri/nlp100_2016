# coding=utf-8

import mk05

paradise = set(mk05.n_gram("paraparaparadise", 2, "moji"))
paragraph = set(mk05.n_gram("paragraph", 2, "moji"))

print paradise | paragraph  # 和
print paradise & paragraph  # 積
print paradise - paragraph  # 差
print "se" in paradise
print "se" in paragraph
