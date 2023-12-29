fruits = {
  "apple": 130,
  "avocado": 50,
  "banana": 110,
  "cantalope": 50,
  "grapefruit": 60,
  "grapes": 90,
  "honeydew melon": 50,
  "kiwifruit": 90,
  "lemon": 15,
  "lime": 20,
  "nectarine": 60,
  "orange": 80,
  "peach": 60,
  "pear": 100,
  "pineapple": 50,
  "plums": 70,
  "strawberries": 50,
  "sweet cherries": 100,
  "tangerine": 50,
  "watermelon": 80,
}
i = 0
item = input("Item: ")
while (True):
    if fruits.get(item.lower()) == None:
        break
    else:
        print("Calories: " + str(fruits.get(item.lower())))
        break
    #Determines calories out of a dict of values