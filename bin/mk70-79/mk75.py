# coding=utf-8

"""
75. 素性の重み
73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
"""

"""
$ cat baseline.model | grep -v '@classias' | sort -g -r | head -10
1.34669	remark
1.28551	beauti
1.21083	delight
1.15719	enjoy
1.02745	rich
1.01796	nuanc
1.01322	hilari
0.999848       	strength
0.987994       	rivet
0.978798       	entertain

$ cat train.model | grep -v "@classias" | sort -g -r | head -10
1.38847	beauti
1.21577	remark
1.18351	delight
1.16583	enjoy
1.04952	entertain
0.990916       	hilari
0.979227       	cultur
0.944894       	power
0.924283       	move
0.907597       	portrait

$ cat baseline.model | grep -v '@classias' | sort -g | head -10
-1.86882       	bore
-1.5924	fail
-1.41942       	bad
-1.29345       	routin
-1.26589       	lack
-1.17431       	disguis
-1.04565       	intent
-1.01845       	alreadi
-1.00528       	video

$ cat train.model | grep -v '@classias' | sort -g | head -10
-1.59522       	bore
-1.49475       	bad
-1.3192	lack
-1.29905       	fail
-0.978067      	routin
-0.869421      	titl
-0.851186      	thin
-0.843646      	doesn't
-0.840025      	disguis
"""
