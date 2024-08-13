names = input().split()

n = [i[0] for i in names]

print("Самостоятельно" if len(n) == len(set(n)) else "Группа")
