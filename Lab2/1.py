# kontynuacja Lab1
#--------------------zad. 1------------------------------------------------
a = float(input('Podaj długosc boku a: '))
b = float(input('Podaj długosc boku b: '))

print('Pole prostokąta o bokach:', a,b, 'wynosi:', a*b)
print('Obwód prostokąta o bokach:', a,b, 'wynosi:', (a+b)*2)

#---------------------zad.1.1
print(f'Pole prostokąta o bokach: {a}, {b} wynosi: {a*b : {10}.{2}}') # {nazwa zmiennej : {10} – szerokość całego pola, .{2}-cyfry po przecinku
print(f'Pole prostokąta o bokach: {a}, {b} wynosi: {(a+b)*2 : {10}.{2}}')

#test: 1.1  2.2
