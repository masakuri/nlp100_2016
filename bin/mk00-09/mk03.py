# coding=utf-8

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.strip(".")
wl = s.split()
pi = ""
for word in wl:
    pi = pi + str(len(word.strip(",")))
print pi
