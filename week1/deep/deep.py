def main(user_input):
    str_user_input = user_input.strip().replace("-", " ").lower()
    match str_user_input:
        case "42" | "forty two":
            print("Yes")
        case _:
            print("No")

if __name__ == "__main__":
    user_input = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    main(user_input)

