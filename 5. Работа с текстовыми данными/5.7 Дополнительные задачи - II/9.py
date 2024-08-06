s = input()

field = " 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 "

print("Игровое поле:")
print(field)
print("Ваш ход:")

for i in field.replace(s[0], s[1]):
    if i.isdigit() and i != "0":
        i = " "
    elif i == "x":
        i = "X"
    print(i, end="")
