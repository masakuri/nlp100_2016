# coding=utf-8

import re

with open("../../data/nlp.txt", "r") as f:
    pattern = re.compile(r"(\.|\;|\?|\!)\ [A-Z]")
    
