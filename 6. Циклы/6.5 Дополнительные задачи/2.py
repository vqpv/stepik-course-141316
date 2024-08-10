w_1, w_2, w_3, w_4 = input(), input(), input(), input()

print("Открыть" if w_1 == w_1[::-1] or w_2 == w_2[::-1] or w_3 == w_3[::-1] or w_4 == w_4[::-1] else "Выбросить")
