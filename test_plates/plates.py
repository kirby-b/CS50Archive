def main():
    plate = input("Plate: ")
    if isValid(plate):
        print("Valid")
    else:
        print("Invalid")


def isValid(s):
    i = 0
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    while(i < len(s)):
        if s[i].isnumeric() and s[i] == "0":
            return False
        if s[i].isnumeric() and s[i] != "0":
            i = 0
            break
        i = i + 1
    while(i < len(s)):
        if s[i].isnumeric():
            if s[i:].isnumeric() == False:
                return False
        if s[i].isnumeric() == False and s[i].isalpha() == False:
            return False
        i = i + 1
    return True
#Same as plates but for testing
main()