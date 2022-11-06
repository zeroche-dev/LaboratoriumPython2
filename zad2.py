# Taking input from the user
# operation = input("Dzialanie: ");
# a = int(input("Podaj liczbe A: "));
# b = int(input("Podaj liczbe B: "));
#
# result = eval(f"{a} {operation} {b}");
#
# print(f"Wynik: {result}");
#


operation = input("Dzialanie: ");
a = int(input("Podaj liczbe A: "));
b = int(input("Podaj liczbe B: "));

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '/':
    if a == 0 or b == 0:
        result = 0
    else:
        result = a / b
elif operation == '*':
    result = a * b
else:
    result = 0


print(f"Wynik: {result}");



