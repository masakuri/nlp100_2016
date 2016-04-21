# coding=utf-8

import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
sl = s.split()
typo_s = ""

for word in sl:
    if len(word) > 4:
        start = word[0]
        end = word[-1]
        middle = word.lstrip(start).rstrip(end)
        middle_ls = list(middle)
        random.shuffle(middle_ls)
        middle_word = "".join(middle_ls)
        typo_s = typo_s + start + middle_word + end + " "
    else:
        typo_s = typo_s + word + " "
print typo_s
