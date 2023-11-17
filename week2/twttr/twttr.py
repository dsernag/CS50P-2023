def main():
    usr_input = input("Input: ").strip()
    output = ""
    for letter in usr_input:
        if letter.lower() in "aeiou":
            continue
        else:
            output += letter
    print(f"Output: {output}")


if "__main__" == __name__:
    main()