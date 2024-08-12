from string import ascii_lowercase

s = input().lower()
result = ""

for i, j in enumerate(s):
    if j in ascii_lowercase:
        result += ascii_lowercase[::-1][ascii_lowercase.find(s[i])]
    else:
        result += j

print(result)
