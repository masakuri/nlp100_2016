# coding=utf-8

import mk20, re

def uk_base_info():
    uk = mk20.uk().split("\n")

    for i, line in enumerate(uk):
        # print line
        if "基礎情報" in line:
            info_start = i + 1  # 基礎情報の開始位置保存
        elif line == "}}":
            info_end = i - 1    # 基礎情報の終了位置保存
            break

    base_info = dict()
    pattern = re.compile(r"\|(?P<key>.+?)=(?P<value>.+)")

    for i in range(info_start, info_end + 1):
        p = re.search(pattern, uk[i])
        if p:
            base_info[p.group("key")] = p.group("value")

    return base_info

if __name__ == '__main__':
    base_info = uk_base_info()
    for k, v in base_info.iteritems():
        print k + " : " + v


"""
> python mk25.py
国際電話番号  :  44
GDP値  :  2兆3162億<ref name="imf-statistics-gdp" />
水面積率  :  1.3%
確立形態2  :  [[グレートブリテン王国]]建国<br />（[[連合法 (1707年)|1707年連合法]]）
略名  :  イギリス
GDP値元  :  1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>
...
確立形態4  :  現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更
...
"""
