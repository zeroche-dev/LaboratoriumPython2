print('''Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie''')
d = int(input('Wpisz numer operacji: '))  # 4
a1 = float(input('Wpisz argument1: '))
a2 = float(input('Wpisz argument2: '))

if d == 1:
    w = a1 + a2
elif d == 2:
    w = a1 - a2
elif d == 3:
    w = a1 * a2
elif d == 4:
    if a2 == 0:
        print('nie możemy dzielić przez zero')
        exit()
    else:
        w = a1 / a2
elif d == 5:
    w = a1 ** a2
else:
    print('błędna operacja')
    exit()

print(f'wynik = {w}')

