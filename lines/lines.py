import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit()
    elif not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit()
    else:
        print(counter(sys.argv[1]))
    #Gets the file for reading

def counter(python_file):
    ignoredLines = 0

    with open(python_file, "r") as lines:

        # Get the total number of lines.
        totalLines = list(enumerate(lines.readlines(), start=1))

        # Go over every line and check if it has code.
        for line_number, lines in totalLines:
            if (lines.strip().startswith("#") or lines.strip().startswith("\n") or lines.isspace()):
                ignoredLines += 1

    return int(totalLines[-1][0]) - ignoredLines
    #Outputs number of lines in a file
if __name__ == "__main__":
    main()