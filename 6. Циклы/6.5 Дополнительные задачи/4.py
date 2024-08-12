s = input()

print("".join([i for i in s if i.isalpha() or i == " "][::-1]))
