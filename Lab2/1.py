# Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
# • Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
# • Dla osób powyżej 18 roku życia bilet kosztuje 20zł.
# Przykład: Wprowadź wiek klienta: 5
# Cena biletu: 10zł

x=int(input("Ile masz lat: "))
if x < 4:
    y = 0
elif x <= 18:
    y = 10
else:
    y = 20
print(f"Bilet kosztuje: {y} zł")