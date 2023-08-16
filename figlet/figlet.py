import sys
import random
from pyfiglet import Figlet
fig = Figlet()
if len(sys.argv) == 1:
    randFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    randFont = False
else:
    print("Invalid usage")
    sys.exit(1)

if randFont == False:
    try:
        fig.setFont(font = sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(fig.getFonts())

sentence = input("Input: ")

print("Output: ")

print(fig.renderText(sentence))