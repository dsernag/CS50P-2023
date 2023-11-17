def main(user_input):
    str_user_input = user_input.strip().lower()
    aa, inter, bb = str_user_input.split(" ")
    aa = float(aa)
    bb = float(bb)

    match inter:
        case "+":
            print(f"{aa + bb}")
        case "-":
            print(f"{aa - bb}")
        case "*":
            print(f"{aa * bb}")
        case "/":
            print(f"{aa / bb}")
        case _:
            print("Error")


if __name__ == "__main__":
    user_input = input("Expression: ")
    main(user_input)

