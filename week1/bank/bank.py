def main(user_input):
    str_user_input = user_input.strip().lower()
    user_words = str_user_input.split()

    if "hello" in user_words[0]:
        print("$0")
    elif str_user_input[0] == "h":
        print("$20")
    else:
        print("$100")
#
if __name__ == "__main__":
    user_input = input("Greeting: ")
    main(user_input)

