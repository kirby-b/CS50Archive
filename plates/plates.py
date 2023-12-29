def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    if len(s) > 6 or len(s) < 2:
        return False
    #Validates length
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    #Validates numbers in it
    while(i < len(s)):
        if s[i].isnumeric() and s[i] == "0":
            return False
        if s[i].isnumeric() and s[i] != "0":
            i = 0
            break
        i = i + 1
    #Validates plate to make sure it has no zeros
    while(i < len(s)):
        if s[i].isnumeric():
            if s[i:].isnumeric() == False:
                return False
        if s[i].isnumeric() == False and s[i].isalpha() == False:
            return False
        i = i + 1
    #Validates to make sure they have no numbers next to each other
    return True
    #Validates a license plate
main()