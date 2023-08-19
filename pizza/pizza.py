import os
import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    else:
        readEZ(sys.argv[1])


def readEZ(user_input):
    """Import CSV and print tabulate grid."""
    with open(user_input, "r") as csvFile:
        table = csv.DictReader(csvFile, delimiter=",")
        # Pass the table as a dict and tell tabulate to use "keys" as headers.
        print(tabulate(table, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()