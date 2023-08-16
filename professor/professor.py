import random


def main():
    level = get_level()
    print(level)
    generate_integer(int(level))

def get_level():
    level = input("Level: ")
    if(level.isdigit() == False or int(level) < 1 or int(level) > 3):
        get_level()
    else:
        return level

def generate_integer(level):
    num1 = 0
    num2 = 0
    wrong = 0
    correct = 0
    i = 0
    while(i <= 10):
        if(level == 1):
            num1 = random.randint(1,9)
            num2 = random.randint(1,9)
        if(level == 2):
            num1 = random.randint(10,99)
            num2 = random.randint(10,99)
        if(level == 3):
            num1 = random.randint(100,999)
            num2 = random.randint(100,999)
        sum = num1 + num2
        ans = input(str(num1) + " + " + str(num2) + " = ")
        if(int(sum) != int(ans) and wrong != 3):
            print("EEE")
            wrong = wrong + 1
        elif (wrong == 3):
            print(str(num1) + " + " + str(num2) + " = " + str(sum))
        else:
            i = i + 1
            correct = correct + 1
    print("Score: " + str(correct))
if __name__ == "__main__":
    main()