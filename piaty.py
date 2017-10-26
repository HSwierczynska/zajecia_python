import re
#regular expressions

plik = open("PoliMorf-0.6.7.tab", "r", encoding="utf-8")

tekst = "Test test test"


ciag = re.split('[\s,.+]' + tekst.lower())

slownik={}
for line in plik:
    temporary = line.split("\t")
    slownik[temporary[0].lower()]= temporary[1].lower()


for slowo in ciag:
    print(slownik[slowo])


while True:
    szukany=input("Podaj wyraz: ").lower()

    try:
        print(slownik[search])

    except KeyError:
        print ("Slowo " + search + " nie wystepuje w slowniku")
