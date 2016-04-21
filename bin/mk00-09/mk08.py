# coding=utf-8

def cipher(text):
    replace = ""
    for word in text:
        if word.islower():
            replace = replace + chr(219 - ord(word))
        else:
            replace = replace + word
    return replace

if __name__ == '__main__':
    text = "Kurihara Masatoshi"
    print cipher(text)
