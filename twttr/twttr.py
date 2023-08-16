name = input("Input: ")
print("Output: ", end = "")
length = len(name)
i = 0
while i < length:
    if name[i].lower() == "a" or name[i].lower() == "e" or name[i].lower() == "i" or name[i].lower() == "o" or name[i].lower() == "u":
        print("", end = "")
    else:
        print(name[i], end = "")
    i = i + 1