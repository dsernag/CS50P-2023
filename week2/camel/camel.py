def main():
    camelCase = input("camelCase: ").strip()
    snake_case = ""
    for index, letter in enumerate(camelCase):
        if index == 0 or letter.islower():
            snake_case += letter.lower()
        else:
            snake_case += f"_{letter.lower()}"
    print(f"snake_case: {snake_case}")

if __name__ == "__main__" :
    main()