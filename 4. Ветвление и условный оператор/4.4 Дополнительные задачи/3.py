day = int(input())
month = input()

if month == "Январь":
    if day in (1, 19):
        print("Козерог")
    else:
        print("Водолей")
elif month == "Февраль":
    if day in (1, 18):
        print("Водолей")
    else:
        print("Рыбы")
elif month == "Март":
    if day in (1, 20):
        print("Рыбы")
    else:
        print("Овен")
elif month == "Апрель":
    if day in (1, 19):
        print("Овен")
    else:
        print("Телец")
elif month == "Май":
    if day in (1, 20):
        print("Телец")
    else:
        print("Близнецы")
elif month == "Июнь":
    if day in (1, 20):
        print("Близнецы")
    else:
        print("Рак")
elif month == "Июль":
    if day in (1, 22):
        print("Рак")
    else:
        print("Лев")
elif month == "Август":
    if day in (1, 22):
        print("Лев")
    else:
        print("Дева")
elif month == "Сентябрь":
    if day in (1, 22):
        print("Дева")
    else:
        print("Весы")
elif month == "Октябрь":
    if day in (1, 22):
        print("Весы")
    else:
        print("Скорпион")
elif month == "Ноябрь":
    if day in (1, 21):
        print("Скорпион")
    else:
        print("Стрелец")  
elif month == "Декабрь":
    if day in (1, 21):
        print("Стрелец")
    else:
        print("Козерог")
