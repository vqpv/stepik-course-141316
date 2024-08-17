from string import ascii_uppercase


n = int(input())

for i in range(n + 1):
    if i == 0:
        print("Игровое поле:\n   ", end="")
        print(*list(ascii_uppercase[:n]))
    else:
        print(str(i).rjust(2) + " ~" * n)
