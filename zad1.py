# Taking input from the user
age = int(input("Podaj wiek"));

if age < 4:
    price = 0
elif age <= 18:
    price = 10
else:
    price = 20

print(f"Cena biletu: {price}");


