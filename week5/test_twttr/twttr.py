def main():
    usr_input = input("Input: ")
    output = shorten(usr_input)
    print(f"Output: {output}")

def shorten(word):
    output = ""
    for letter in word.strip():
        if letter.lower() in "aeiou":
            continue
        else:
            output += letter
    return output.strip()

if __name__ == "__main__":
    main()