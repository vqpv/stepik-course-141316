l, b, h = int(input()), int(input()), int(input())

if l <= 15 and b <= 15 and h <= 15:
    print("Коробка №1")
elif l > 200 or b > 200 or h > 200:
    print("Упаковка для лыж")
elif 15 <= l < 50 and 15 <= b < 50 and 15 <= h < 50:
    print("Коробка №2")
else:
    print("Коробка №3")
