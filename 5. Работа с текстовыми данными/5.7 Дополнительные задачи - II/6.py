time = input()

t, i = time.split()

if i == "PM":
    h, m = t.split(":")
    print(f"{int(h) + 12}:{m}")
else:
    print(t)
