a, b, c = int(input()), int(input()), int(input())

if a == b and b == c:
    print("Равносторонний")
elif a == b or a == c or c == b:
    print("Равнобедренный")
elif a not in (b, c) and b != c:
    print("Разносторонний")
else:
    print("Такого треугольника не существует")
