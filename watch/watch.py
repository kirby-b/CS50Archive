import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    #Extract a YouTube URL from a given string of embedded HTML using regex patterns.
    try:
        urlPattern = re.search('(?<=embed\/).*?(?=")', s)
        return "https://youtu.be/" + urlPattern.group(0)
    except Exception:
        return None


if __name__ == "__main__":
    main()