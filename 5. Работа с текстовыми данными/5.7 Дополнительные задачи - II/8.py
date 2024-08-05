date = input()

d, m, y = date.split(".")

def sum_nums(lst_n):
    result = sum(map(int, list(str(lst_n))))
    while result // 10 >= 1:
        result = sum(map(int, list(str(result))))
    return result

sum_d = sum_nums(d)
sum_m = sum_nums(m)
sum_y = sum_nums(y)

print(sum_nums(sum_d + sum_m + sum_y))
