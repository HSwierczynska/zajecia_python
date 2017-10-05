dniTygodnia=["poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela"]
for dzien in dniTygodnia:
        dlugosc = len(dzien)
        temp = dlugosc %3
        print(dzien[temp])

