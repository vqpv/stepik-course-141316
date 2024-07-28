s_1 = input()
s_2 = input()

if len(s_1) > len(s_2):
    print("Первая строка длиннее.")
elif len(s_1) < len(s_2):
    print("Вторая строка длиннее.")
if len(s_1) == len(s_2):
    print("Строки равны.")
