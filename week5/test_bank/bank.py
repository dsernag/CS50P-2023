def main():
    str_user_input = input("Greeting: ")
    print(f"${value(str_user_input)}")

def value(greeting):
    greeting = greeting.strip().lower()
    user_words = greeting.split()
    if "hello" in user_words[0]:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

