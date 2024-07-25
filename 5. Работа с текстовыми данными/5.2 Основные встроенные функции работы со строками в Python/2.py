f_name, l_name = input().split()

if f_name.isalpha() and l_name.isalpha():
    print(f"Привет, {f_name} {l_name}!")
else:
    print("Некорректные имя или фамилия")
