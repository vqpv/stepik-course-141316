s = input()

words = s.split()

print("".join([i[0] for i in words]).upper())
