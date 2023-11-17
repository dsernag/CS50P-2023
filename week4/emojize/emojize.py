import emoji

def main():
    str_input = input("Input: ")
    print(emoji.emojize(str_input, language="alias"))


if "__main__" == __name__:
    main()