def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
    #Calculates tip for your meal

def dollars_to_float(d):
    d = d.replace("$", "")
    return float(d)
    #converts to a float

def percent_to_float(p):
    p = p.replace("%", "")
    p = float(p)
    return p/100
    #converts to a float

main()