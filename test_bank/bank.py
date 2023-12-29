def main():
    greet = input("Greeting: ")
    greet = greet.lower().strip()
    print(value(greet))

def value(greet):
    if ("hello" in greet):
        return("$0")
    elif (greet.startswith("h")):
        return("$20")
    else:
        return("$100")
#Same as bank but for testing

if __name__ == "__main__":
    main()