months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while (True):
    date = input("Date: ")
    try:
        m, d, y = date.replace(" ","").split("/")
        if( 1 <= int(d) <= 31 and 1 <= int(m) <= 12):
            break
    except:
        try:
            m, d, y = date.split(" ")
            if ("," not in d):
                raise ValueError()
            d = d.replace(",","")
            m = months.index(m) + 1
            if( 1 <= int(d) <= 31 and 1 <= int(m) <= 12):
                break
        except:
            print()
            pass
print(y + "-{:02d}-".format(int(m)) + "{:02d}".format(int(d)))