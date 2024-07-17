weight = float(input())
height = float(input())

i = weight / (height * height)

if i < 18.5:
    print("Недостаточный вес")
elif 18.5 < i <= 24.9:
    print("Нормальный вес")
elif 24.9 < i <= 29.9:
    print("Избыточный вес")
elif i > 29.9:
    print("Ожирение")
