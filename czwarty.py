plik = open("PoliMorf-0.6.7.tab", "r", encoding="utf8")

zmiennaSlownikowa={}

#zmiennaSlownikowa[klucz]=wyraz

szukanyWyraz = input("Podaj wyraz ")



for linia in plik:
   # print(linia.split("\t"))
   zmiennaTemp = linia.split("\t")
   zmiennaSlownikowa[zmiennaTemp[0]] = zmiennaTemp[1]

print(zmiennaSlownikowa[szukanyWyraz])




