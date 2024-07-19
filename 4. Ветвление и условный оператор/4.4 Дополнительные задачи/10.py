user = input()
password = input()

if user != "user123":
    print("Пользователь не найден.")
elif user == "user123" and password != "pass123":
    print("Неверный пароль.")
elif user == "user123" and password == "pass123":
    print("Вход выполнен успешно!")
