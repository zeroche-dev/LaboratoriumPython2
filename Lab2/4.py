znak = input('Wprowadź znak: ')

if znak >= 'a' and znak <= 'z':
    print('Wprowadzono małą literę.')
elif znak >= 'A' and znak <= 'Z':
    print('Wprowadzono dużą literę.')
else:
    print('Wprowadzony znak nie jest literą.')