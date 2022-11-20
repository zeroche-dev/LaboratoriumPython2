# # Utwórz listę zestaw_1 zawierającą liczby losowe z przedziału [1, 10]. Liczbę elementów listy podaje # użytkownik. Wyświetl listę import random #
# #
# import random
#
# zestaw_1 = []
#
# x = int(input("podaj liczbę x: "))
# y = int(input("podaj liczbę y: "))
#
# for i in range(x):
#     zestaw_1.append(random.randint(1, 10))
#
# zestaw_1 = [random.randint(1, 10) for i in range(x)]
# print("lista x:", zestaw_1)
# zestaw_2 = [random.randint(5, 15) for i in range(y)]
# print("lista x:", zestaw_2);
#
#
# z = int(input("Podaj liczbe do sprawdzniea"))
#
# zestaw_1_2 = zestaw_1 + zestaw_2;
# print(zestaw_1_2);
#
# zestaw_1_2.sort();
#
# print(zestaw_1_2);
#

import random

punkty = [round(random.uniform(0, 50), 2) for i in range(15)]

print(punkty)

m = min(punkty)
mx = max(punkty)
print(f"Min {m}, Max: {mx}")

avg = round(sum(punkty) / len(punkty), 2)

print(f"Average: {avg}")












