greet = input("Greeting: ")
greet = greet.lower().strip()

if ("hello" in greet):
    print("$0")
elif (greet.startswith("h")):
    print("$20")
else:
    print("$100")
#Prints payout based on input