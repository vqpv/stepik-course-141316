num = float(input())

s_num = str(num)
a, b = s_num.split(".")

if int(b[-1]) >= 5:
    if b[0] == "9":
        print(int(a) + 1)
    else:
        b = str(int(b) + 10)[:-1].rstrip("0")
        print(f"{a}.{b}")
else:
    print(f"{a}.{b[:-1]}")
