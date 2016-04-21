# coding=utf-8

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
wl = s.split()
wd = dict()
index1 = (1, 5, 6, 7, 8, 9, 15, 16, 19)
for num, word in enumerate(wl):
    if int(num) + 1 in index1:
        wd[num + 1] = word[0:1]
    else:
        wd[num + 1] = word[0:2]
print wd
