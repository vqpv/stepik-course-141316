n = int(input())

f_1 = f_2 = 1

while n - 2 > 0:
    f_1, f_2 = f_2, f_1 + f_2
    n -= 1

if n == 0:
    print(0)
else:
    print(f_2)
