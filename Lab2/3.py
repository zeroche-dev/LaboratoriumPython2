print("""Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie""")
c = int(input("Enter +(1),-(2),/(4),*(3)"))
if c < 1 or c > 5:
    print("Not selected any of numbers")
    exit()

a = int(input("Enter first number"))
b = int(input("Enter second number"))
if c == 1:
  w = a + b
elif c == 2:
  w = a - b
elif c == 3:
    w = a * b
elif c == 4:
    if b == 0:
        print("Can't devide on 0")
        exit()
    else:
         w = a / b

print(f'wynik = {w}')