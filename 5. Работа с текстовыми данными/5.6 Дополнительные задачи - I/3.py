num = input()

m = len(num) // 2

if sum([int(i) for i in num[:m]]) == sum([int(i) for i in num[m:]]):
    print("Счастливый билет")
else:
    print("Несчастливый билет")
