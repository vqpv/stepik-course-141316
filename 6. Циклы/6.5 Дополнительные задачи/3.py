s = input()

result = "Уникальный"

for i in s:
    if s.count(i) > 1:
        result = "Повтор"
        break

print(result)
