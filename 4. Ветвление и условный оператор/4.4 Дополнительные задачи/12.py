name = input()

name_len = len(name)

if name_len <= 22:
    if name_len % 2 == 0:
        result = ((26 - name_len) // 2) - 1
        print("-" * result + " " + name + " " + "-" * result)
        print("-" * 26)
    else:
        result = ((26 - name_len) // 2) - 1
        print("-" * (result + 1) + " " + name + " " + "-" * result)
        print("-" * 26)  
else:
    print("Имя превышает максимально допустимую длину")
