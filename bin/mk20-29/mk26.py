# coding=utf-8

import mk25, re

base_info = dict()
def remove_enph():
    pattern = re.compile(r"\'{2,5}")
    for k, v in mk25.uk_base_info().iteritems():
        if re.search(pattern, v):
            v = re.sub(r"\'{2,5}", "", v)
        base_info[k] = v
    return base_info

if __name__ == '__main__':
    base_info = remove_enph()
    for k, v in base_info.iteritems():
        print k + " : " + v

"""
> python mk26.py
GDP値  :  2兆3162億<ref name="imf-statistics-gdp" />
水面積率  :  1.3%
確立形態2  :  [[グレートブリテン王国]]建国<br />（[[連合法 (1707年)|1707年連合法]]）
略名  :  イギリス
GDP値元  :  1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>
...
確立形態4  :  現在の国号「グレートブリテン及び北アイルランド連合王国」に変更
...
"""
