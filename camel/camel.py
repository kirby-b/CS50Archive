name = input("camelCase: ")
print("snake_case:", end = "")
length = len(name)
i = 0
while i < length:
    if name[i].isupper():
        print("_" + name[i].lower(), end = "")
    else:
        print(name[i], end = "")
    i = i + 1;