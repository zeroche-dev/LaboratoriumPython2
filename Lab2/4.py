litera = input("podaj literę:" )
roznica = ord('a') - ord('A')

if 'a' <= litera <= 'z' :
    print(chr(ord(litera) - roznica))
elif 'A' <= litera <= 'Z':
    nowa = ord(litera) + roznica
    znak = chr(nowa)
    print(znak)
else :
    print("to nie jest litera")



# ord(znak) - zwraca kod ASCII
# chr(kod) - zwraca znak