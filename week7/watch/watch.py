import re

def main():
    print(parse(input("HTML: ")))

def parse(string):
    pattern = r'^<iframe(?:.+)?src="(?:https?://)?(?:www\.)?youtube\.com/embed/(\w+)"(?:.+)?(?:</iframe>)$'
    if result := re.search(pattern, string):
        return f"https://youtu.be/{result.group(1)}"

if __name__ == "__main__":
    main()