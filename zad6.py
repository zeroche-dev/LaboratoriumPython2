# Taking input from the user
a = int(input("Podaj liczbe A: "))
b = int(input("Podaj liczbe B: "))

if a > b:
    (a, b) = (b, a)
while a <= b:
    if a % 2 == 1:
        a+=1
        continue
    print(a, end=' ')
    a+=1

