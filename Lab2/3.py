print('''Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie''')
x = int(input("wpisz numer operacji "))
y = float(input("podaj argument 1 "))
z = float(input("podaj argument 2 "))
if x == 1:
    wynik = y + z
elif x ==2:
    wynik = y - z
elif x ==3:
    wynik = y * z
elif x ==4:
    if z == 0:
        print('Błąd')
        exit()
    wynik = y / z
elif x ==5:
    wynik = y ** z
else:
    print("niepoprawne operacje ")
    exit()
print(wynik)