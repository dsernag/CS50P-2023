def main():
    result = prompt_convert()
    print_result(result)

def prompt_convert():
    xx, yy = prompt_user()
    while xx > yy:
        xx, yy = prompt_user()
    return frac_to_dec(xx, yy)

def prompt_user():
    while True:
        try:
            user_input = input("Fraction: ").split("/")
            xx = int(user_input[0])
            yy = int(user_input[1])
            return xx, yy
        except:
            pass

def frac_to_dec(xx, yy):
    while True:
        try:
            return (xx / yy) * 100
        except:
            xx, yy = prompt_user()

def print_result(result):
    if result >= 99:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(f"{result:.0f}%")

if "__main__" == __name__:
    main()