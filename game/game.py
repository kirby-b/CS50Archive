import random
while(True):
    level = input("Level: ")
    if (level.isdigit() == True and int(level) > 2):
        break
while(True):
    guess = input("Guess: ")
    if (guess.isdigit() == True and int(guess) < int(level)):
        break
hiddenNum = random.randrange(1, int(level))
while(True):
    if (int(guess) > hiddenNum):
        print("Too large!")
        guess = input("Guess: ")
    elif (int(guess) < hiddenNum):
        print("Too small!")
        guess = input("Guess: ")
    else:
        print("Just right!")
        break
    #Plays a number guessing game