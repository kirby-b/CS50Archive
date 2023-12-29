def main():
    while(True):
        fuelFraction = input("Fraction: ")
        try:
            x, y = fuelFraction.split("/")
            numer = int(x)
            denom = int(y)
            if (numer > denom):
                raise ValueError()
            elif ((numer / denom) >= 0.99):
                print("F")
                break
            elif ((numer / denom) <= 0.01):
                print("E")
                break
            else:
                to_percent = (numer / denom) * 100
                result = int(round(to_percent))
                print(str(result) + "%")
                break
        except (ValueError, ZeroDivisionError):
            pass
        #Takes a number percent and tells you how full the tank is

main()