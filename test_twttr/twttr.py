def main():
    name = input("Input: ")
    print("Output: ", end = "")
    print(shorten(name))
def shorten(name):
    length = len(name)
    i = 0
    shortened = ""
    while i < length:
        if name[i].lower() == "a" or name[i].lower() == "e" or name[i].lower() == "i" or name[i].lower() == "o" or name[i].lower() == "u":
            shortened = shortened + ""
        else:
            shortened = shortened + name[i]
        i = i + 1
    return shortened
if __name__ == "__main__":
    main()

#Same as twttr but for testing