nameList = []
while (True):
    try:
        name = input("")
        nameList.append(name)#Gets names

    except(EOFError):
        if (len(nameList) > 1):
            x = 1
            goodbye = ""
            while x < len(nameList):
                goodbye = goodbye + nameList[x-1] + ", "
                x = x + 1
                #Makes a string out of the names
            print("Adieu, adieu, to " + goodbye + "and " + nameList[-1])
            #Prints the message
        elif (len(nameList) == 1):
            print("Adieu, adieu, to " + nameList[0])
        exit()
