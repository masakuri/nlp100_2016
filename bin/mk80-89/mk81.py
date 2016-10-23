# coding=utf-8

"""
81. 複合語からなる国名への対処
英語では，複数の語の連接が意味を成すことがある．例えば，アメリカ合衆国は"United States"，イギリスは"United Kingdom"と表現されるが，"United"や"States"，"Kingdom"という単語だけでは，指し示している概念・実体が曖昧である．そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，複合語の意味を推定したい．しかしながら，複合語を正確に認定するのは大変むずかしいので，ここでは複合語からなる国名を認定したい．

インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，スペースをアンダーバーに置換せよ．例えば，"United States"は"United_States"，"Isle of Man"は"Isle_of_Man"になるはずである．
"""

"""
国名リストは以下から拝借
http://www.countries-list.info/Download-List
"""

import sys

f = open("country_name.txt", "r")   # 入手した国名リスト読み込み
countries_list = f.read().split("\n")   # 国名リスト作成
f.close()
wiki_data = sys.stdin
for line in wiki_data:
    for country_name in countries_list:
        # 愚直に記事の各行に対して国名リストと一致した複合語の国名のスペースをアンダーバーに置換
        line = line.replace(country_name, country_name.replace(" ", "_"))
    print line,

"""
$ time zcat enwiki.txt.gz| python mk81.py | gzip > enwiki_countryname.txt.gz
zcat enwiki.txt.gz  0.76s user 0.05s system 0% cpu 1:28.80 total
python mk81.py  84.91s user 0.39s system 95% cpu 1:28.92 total
gzip > enwiki_countryname.txt.gz  6.46s user 0.10s system 7% cpu 1:28.92 total
$ zcat enwiki_countryname.txt.gz | less
...
... Since the 1890s from France the term libertarianism has often been used as a synonym for anarchism and was used almost exclusively in this sense until the 1950s in the United_States its use as a synonym is still common outside the United_States On the other hand some use libertarianism to refer to individualistic free-market philosophy only referring to free-market anarchism as libertarian anarchismrchism
...
"""

"""
$ time zcat enwiki10.txt.gz| python mk81.py | gzip > enwiki_countryname10.txt.gz
zcat enwiki10.txt.gz  7.53s user 0.39s system 0% cpu 14:50.29 total
python mk81.py  848.22s user 2.86s system 95% cpu 14:50.40 total
gzip > enwiki_countryname10.txt.gz  64.25s user 0.88s system 7% cpu 14:50.40 total
"""
# 1/10
