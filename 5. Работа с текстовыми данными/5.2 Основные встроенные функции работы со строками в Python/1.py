a_1, b_1 = map(int, input().split(","))
a_2, b_2 = map(int, input().split(","))

if a_1 * b_1 > a_2 * b_2:
    print("Квартира А")
else:
    print("Квартира Б")
