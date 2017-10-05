dniTygodnia=["poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela"]
for dzien in dniTygodnia:
    dlugosc = len(dzien)
    if (dlugosc%2==0):
        print ('\n')
        print(dzien)
        for x in range (dlugosc, 0, -1):
            print(x, end=' ')
