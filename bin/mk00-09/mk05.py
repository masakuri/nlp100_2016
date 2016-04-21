# coding=utf-8

def n_gram(text, n, select):
    i = 0
    ngram_ls = list()
    if select == "tango":
        tango_ls = text.split()
        bi_ls = list()
        while(i < len(tango_ls) - 1):
            for j in range(2):
                bi_ls.append(tango_ls[i + j])
            ngram_ls.append(bi_ls)
            bi_ls = list()
            i += 1

    if select == "moji":
        while(i < len(text) - 1):
            ngram_ls.append(text[i:i+n])
            i += 1

    return ngram_ls

if __name__ == '__main__':
    s = "I am an NLPer"
    print n_gram(s, 2, "tango")
