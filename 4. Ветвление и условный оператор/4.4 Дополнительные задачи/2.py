year = int(input())

if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
    print("Високосный год")
else:
    print("Обычный год")
