c = 0

for i in range(1, 22):
    if i % 2 == 1:
        s = ""
        for j in range(51):
            if j % 5 == 0:
                s += "+"
            else:
                s += "-"
    else:
        s = "|"
        if c % 2 == 0: 
            for x in range(1 + 10 * c, 11 + 10 * c):
                if x // 10 == 0:
                    s += f'  {str(x)} |'
                elif 1 <= x // 10 <= 9:
                    s += f' {str(x)} |'
                elif x // 100 >= 1:
                    s += f'{str(x)} |'
        else:
            for z in reversed(range(1 + 10 * c, 11 + 10 * c)):
                if z // 10 == 0:
                    s += f'  {str(z)} |'
                elif 1 <= z // 10 <= 9:
                    s += f' {str(z)} |'
                elif z // 100 >= 1:
                    s += f'{str(z)} |'
        c += 1
    print(s)
