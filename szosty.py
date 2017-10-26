import re

slownik={}
plik = open("PoliMorf- 0.6.7.tab", "r", encoding="utf-8")


for linia in plik.readlines():
    slowo = linia.strip().split('\t')
    try:
        slownik[slowo[0]]=slowo[1] + " "+slowo[2]+" "+slowo[3]
    except:
        slownik[slowo[0]]=slowo[1]+" "slowo[2]


plik.close()

for klucz in slowni:
    if re.search("^arbus .*:voc:.*", slownik[klucz]):
        print klucz
