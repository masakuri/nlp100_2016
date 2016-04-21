# coding=utf-8

import mk27, re

def remove_mark():
    base_info = dict()
    html_pattern = re.compile(r"\<(.+?)\>") # htmlタグ
    inter_pattern = re.compile(r"\[(.+?)\]")    # 内部リンク
    temp_pattern = re.compile(r"\{\{(.+?)\}\}") # テンプレート

    for k, v in mk27.remove_hyper().iteritems():
        v = html_pattern.sub(r"", v)
        v = inter_pattern.sub(r"", v)
        v = temp_pattern.sub(r"\1", v)
        base_info[k] = v
    return base_info

if __name__ == '__main__':
    base_info = remove_mark()
    for k, v in base_info.iteritems():
        print k + " : " + v

"""
> python mk28.py
GDP値  :  2兆3162億
水面積率  :  1.3%
確立形態2  :  グレートブリテン王国建国（連合法 (1707年)|1707年連合法）
略名  :  イギリス
GDP値元  :  1兆5478億
面積値  :  244,820
確立年月日3  :  1801年
面積順位  :  76
通貨  :  スターリング・ポンド|UKポンド (&pound;)
国歌  :  女王陛下万歳|神よ女王陛下を守り給え
確立形態3  :  グレートブリテン及びアイルランド連合王国建国（連合法 (1800年)|1800年連合法）
時間帯  :  ±0
ISO 3166-1  :  GB / GBR
人口統計年  :  2011
元首等氏名  :  エリザベス2世
GDP/人  :  36,727
人口大きさ  :  1 E7
公用語  :  英語（事実上）
最大都市  :  ロンドン
公式国名  :  lang|en|United Kingdom of Great Britain and Northern Ireland英語以外での正式国名:
GDP統計年MER  :  2012
元首等肩書  :  イギリスの君主|女王
面積大きさ  :  1 E11
確立形態4  :  現在の国号「グレートブリテン及び北アイルランド連合王国」に変更
通貨コード  :  GBP
GDP統計年  :  2012
夏時間  :  +1
国旗画像  :  Flag of the United Kingdom.svg
GDP値MER  :  2兆4337億
注記  :
確立年月日1  :  927年／843年
日本語国名  :  グレートブリテン及び北アイルランド連合王国
首相等氏名  :  デーヴィッド・キャメロン
国章リンク  :  （イギリスの国章|国章）
確立年月日2  :  1707年
標語  :  lang|fr|Dieu et mon droit（フランス語:神と私の権利）
確立年月日4  :  1927年
首都  :  ロンドン
首相等肩書  :  イギリスの首相|首相
GDP順位MER  :  5
GDP順位  :  6
人口密度値  :  246
位置画像  :  Location_UK_EU_Europe_001.svg
人口値  :  63,181,775
人口順位  :  22
国際電話番号  :  44
GDP統計年元  :  2012
ccTLD  :  .uk / .gb使用は.ukに比べ圧倒的少数。
確立形態1  :  イングランド王国／スコットランド王国（両国とも連合法 (1707年)|1707年連合法まで）
国章画像  :  ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章
建国形態  :  建国
"""
