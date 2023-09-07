import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    #Return a boolean value on validation of IP using a regex pattern.
    try:
        if (ip.isdigit() == False):
            raise ValueError
        pattern = "^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
        result = re.match(pattern, ip)
        if result == False:
            return False

    except ValueError:
        return False

    else:
        return True


if __name__ == "__main__":
    main()