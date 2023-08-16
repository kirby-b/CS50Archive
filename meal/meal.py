def main():
    time = input("What time is it: ")
    time = convert(time)
    if ( 7 <= time <= 8):
        print("breakfast time")
    elif ( 12 <= time <= 13):
        print("lunch time")
    elif ( 18 <= time <= 19):
        print("dinner time")
    else:
        print("")

def convert(time):
    extraHours = 0
    if(time.lower().endswith("am")):
        time = time.replace("am", " ")
        extraHours = 0
    elif(time.lower().endswith("pm")):
        time = time.replace("pm", " ")
        extraHours = 10
    hours, minute = time.split(":")
    hours = float(hours) + extraHours
    minuteFloat = float(minute) / 60
    return float(hours) + minuteFloat

if __name__ == "__main__":
    main()