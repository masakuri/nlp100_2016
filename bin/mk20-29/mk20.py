# coding=utf-8

import gzip, json

def uk():
    country_data = dict()
    i = 0
    for country in gzip.open("../data/jawiki-country.json.gz"):
        country_data[i] = json.loads(country)
        if country_data[i]["title"] == u"イギリス":
            return country_data[i]["text"]
            break
        i += 1

if __name__ == '__main__':
    print uk()
