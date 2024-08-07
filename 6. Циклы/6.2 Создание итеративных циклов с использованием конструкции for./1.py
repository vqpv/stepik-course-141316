s = input().lower()

letters = ('a', 'e', 'i', 'o', 'u')
c = 0

for i in s:
    if i in letters:
        c += 1

print(c)
