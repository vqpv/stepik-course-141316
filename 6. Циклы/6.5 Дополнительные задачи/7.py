pin = "9681"
c = 0

while c < 3:
    input_pin = input()
    if len(input_pin) == 4:
        if input_pin == pin:
            print("КОРРЕКТНЫЙ ПИН")
            break
        else:
            print("НЕПРАВИЛЬНЫЙ ПИН")
            c += 1
            if c == 3:
                print("КАРТА ЗАБЛОКИРОВАНА")
                break
    else:
        print("НЕПРАВИЛЬНЫЙ ФОРМАТ ПИН")
