grocery_list = {}
while (True):
    try:
        item = input()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except(EOFError, KeyboardInterrupt):
        for x in sorted(grocery_list):
            print(str(grocery_list[x]) + " " + x.upper())
        break
    #Outputs a grocery list and sorts it