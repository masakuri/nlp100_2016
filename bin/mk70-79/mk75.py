# coding=utf-8

"""
75. 素性の重み
73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
"""

"""
$ cat baseline.model | grep -v '@classias' | sort -g -r | head -10
1.5613 	engross
1.53987	refresh
1.41034	unexpect
1.28457	remark
1.28194	beauti
1.27526	cinema
1.22712	delight
1.18741	solid
1.17976	examin
1.16101	enjoy

$ cat train.model | grep -v "@classias" | sort -g -r | head -10
1.39418	beauti
1.26501	engross
1.24092	refresh
1.19363	delight
1.18997	remark
1.16708	enjoy
1.13665	unexpect
1.08496	entertain
1.08099	cinema
1.06516	solid

$ cat baseline.model | grep -v '@classias' | sort -g | head -10
-1.88139       	bore
-1.76737       	dull
-1.60592       	fail
-1.49098       	wast
-1.48115       	worst
-1.4396	mediocr
-1.33724       	bad
-1.33572       	flat
-1.30285       	routin
-1.29166       	appar

$ cat train.model | grep -v '@classias' | sort -g | head -10
-1.59529       	bore
-1.57854       	dull
-1.4112	bad
-1.39151       	worst
-1.33474       	lack
-1.30862       	fail
-1.21108       	mediocr
-1.20919       	wast
-1.14107       	flat
-1.06768       	plod
"""
