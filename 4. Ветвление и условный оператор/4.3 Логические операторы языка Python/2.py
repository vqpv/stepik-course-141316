a, b, c = int(input()), int(input()), int(input())

if c < b < a:
    c, a = a, c
elif c < a < b:
    c, b = b, c

if a ** 2 + b ** 2 == c ** 2:
    print("Треугольник является прямоугольным.")
else:
    print("Треугольник не является прямоугольным.")
