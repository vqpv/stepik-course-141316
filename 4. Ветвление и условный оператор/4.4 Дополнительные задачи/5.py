hour = int(input())

if 0 <= hour <= 5:
    print("ночь")
elif 6 <= hour <= 11:
    print("утро")
elif 12 <= hour <= 17:
    print("день")
elif 18 <= hour <= 23:
    print("вечер")
