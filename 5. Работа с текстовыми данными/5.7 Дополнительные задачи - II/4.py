url = input()

if "?v=" in url:
    f_index = url.rfind("=")
else:
    f_index = url.rfind("/")

print(url[f_index + 1:])
