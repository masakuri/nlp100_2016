# coding=utf-8

"""
90. word2vecによる学習
81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
"""

"""
$ time ~/word2vec/word2vec -train ../mk80-89/enwiki_countryname.txt -output w2v.txt -size 300
Starting training using file ../mk80-89/enwiki_countryname.txt
Vocab size: 85470
Words in train file: 11703449
Alpha: 0.000026  Progress: 99.98%  Words/thread/sec: 155.78k  ~/word2vec/word2vec -train ../mk80-89/enwiki_countryname.txt -output w2v.txt   391.01s user 3.87s system 298% cpu 2:12.28 total
"""

import sys
from gensim.models import Word2Vec
import cPickle as pickle
import argparse

def mk86(model):
    print "Input a word to print word vector : ",
    target_word = raw_input()
    target_word = target_word.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_") # United States -> United_States
    print model[target_word]

def mk87(model):
    print "Input two words to calculate cosine similarity : "
    print "word1 : ",
    word1 = raw_input()
    print "word2 : ",
    word2 = raw_input()

    word1 = word1.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_") # United States -> United_States
    word2 = word2.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_") # United States -> United_States
    print model.similarity(word1, word2)

def mk88(model):
    print "Input a word to find words most similar to the word : ",
    target_word = raw_input()
    for k, v in model.most_similar(positive=target_word):
        print k, v

def mk89(model):
    print "Input three words to find words most similar to vec(word1) - vec(word2) + vec(word3) : "
    print "word1 : ",
    word1 = raw_input()
    print "word2 : ",
    word2 = raw_input()
    print "word3 : ",
    word3 = raw_input()

    word1 = word1.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_") # United States -> United_States
    word2 = word2.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_") # United States -> United_States
    word3 = word3.strip(".,!?;:\(\)\[\]\'\"").replace(" ", "_") # United States -> United_States
    for k, v in model.most_similar(positive=[word1, word3], negative=[word2]):
        print k, v


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("-c", "--command", dest = "command", help = "input 86, 87, 88, or 89, 86 : Print word vector, 87 : Calculate cosine similarity, 88 : Find words most similar to some word, 89 : Additive compositionality analogy")
    args = p.parse_args()

#    model = Word2Vec.load_word2vec_format('w2v.txt', binary=False) # 初回実行時のみ
#    pickle.dump(model, open('w2v.dump', 'w'))  # 初回実行時のみ（約45s）

    model = Word2Vec.load("w2v.dump")

    if args.command == "86":
        mk86(model)
    elif args.command == "87":
        mk87(model)
    elif args.command == "88":
        mk88(model)
    elif args.command == "89":
        mk89(model)

"""
$ python mk90.py -c 86
Input a word to print word vector :  United States
[-0.59289598 -0.112545   -0.31538901  0.86996502  1.36431003 -0.91765898
  1.12998402 -0.22202399  1.50643301 -0.44446301  0.02414     0.31549901
  ...
 -0.15607101 -0.112776   -0.97495699 -0.120624   -1.37801695 -0.78561598]

$ python mk90.py -c 87
Input two words to calculate cosine similarity :
word1 :  United States
word2 :  U.S.
0.778583733394

$ python mk90.py -c 88
Input a word to find words most similar to the word :  England
Scotland 0.658398628235
Wales 0.625836849213
Hampshire 0.55825740099
Britain 0.53892737627
Ireland 0.534616172314
Somerset 0.506488025188
Lancashire 0.498837947845
Edinburgh 0.487557947636
Plymouth 0.482953131199
England's 0.47956559062

$ python mk90.py -c 89
Input three words to find words most similar to vec(word1) - vec(word2) + vec(word3) :
word1 :  Spain
word2 :  Madrid
word3 :  Athens
Greece 0.538233101368
Egypt 0.517101287842
Slovakia 0.515290498734
Persia 0.513086020947
Armenia 0.509006381035
Flanders 0.501361310482
Denmark 0.498016893864
Mesopotamia 0.494162887335
Bavaria 0.49394261837
Venice 0.490793168545
"""
# よげ
