num = input()

if num.isdigit():
    while len(num) != 1:
        num = str(sum(map(int, list(num))))
    print(num)
else:
    print("Ошибка")
