import re

def main():
    print(count(input("Text: ")))

def count(string):
    search = re.findall(r'\bum\b', string, re.IGNORECASE)
    return len(search)

if __name__ == "__main__":
    main()