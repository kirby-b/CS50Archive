express = input("Expression: ")

x, y, z = express.split(" ")

xFloat = float(x)
zFloat = float(z)

if (y == "-"):
    print(xFloat - zFloat)
elif (y == "+"):
    print(xFloat + zFloat)
elif (y == "/"):
    print(xFloat / zFloat)
elif (y == "*"):
    print(xFloat * zFloat)