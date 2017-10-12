plik = open("PoliMorf-0.6.7.tab", "r", encoding="utf8")

zmiennaSlownikowa={"szła":"iść","szedł":"iść"}

#zmiennaSlownikowa[klucz]=wyraz

for linia in plik:
   # print(linia.split("\t"))
   zmiennaTemp = linia.split("\t")
   zmiennaSlownikowa[zmiennaTemp[0]] = zmiennaTemp[1]


szukanyWyraz = input("Podaj wyraz ")

print(zmiennaSlownikowa[szukanyWyraz])



