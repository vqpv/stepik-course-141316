from math import ceil


weight = float(input())
country = input()

p_1 = 500
p_2 = 1000

if country == "Россия":
    print(p_1)
else:
    print(p_2 + (ceil(weight) - 1) * p_1)
