owed = 50
while(True):
    print("Amount Due: " + str(owed))
    coin = input("Insert Coin: ")
    if coin == "25" or coin == "10" or coin == "5":
        owed = owed - int(coin)
    if owed <= 0:
        print("Change Owed: " + str(abs(owed)))
        break
    #Gets money and how much is owed