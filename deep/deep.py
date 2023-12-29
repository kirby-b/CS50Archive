print("What is the Answer to the Great Question of Life, the Universe, and Everything?")
ans = input()
ans = ans.strip()
if (ans == "42" or ans.lower() == "forty-two" or ans.lower() == "forty two"):
    print("Yes")
else:
    print("No")
#Its just a reference to an amazing movie