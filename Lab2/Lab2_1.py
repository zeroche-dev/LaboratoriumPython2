# Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
# • Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
# • Dla osób powyżej 18 roku życia bilet kosztuje 20zł.
# Przykład: Wprowadź wiek klienta: 5
# Cena biletu: 10zł

Wiek = int(input("Podaj Wiek: "))
if Wiek < 4:
    Cena = 0
elif Wiek <= 18:
    Cena = 10
else:
    Cena = 20
print(f"Cena Biletu: {Cena}zł")
