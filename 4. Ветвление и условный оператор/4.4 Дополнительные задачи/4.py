human_year = float(input())

if 0 < human_year <= 2:
    print(round(human_year * 10.5, 1))
elif human_year > 2:
    print(round(2 * 10.5 + (human_year - 2) * 4, 1))
else:
    print("Введен неверный возраст")
