import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        if match := re.search(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$', ip):
            numbers = [match.group(1), match.group(2), match.group(3), match.group(4)]
            try:
                if all([256 > int(ii) >= 0 for ii in numbers]):
                    return True
                else:
                    return False
            except:
                return False
        else:
            return False
    except:
        return False
if __name__ == "__main__":
    main()