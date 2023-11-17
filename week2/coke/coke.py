def main():
    # Main variables
    DUE = 50
    print_amount_due(DUE)
    debt_program(DUE)

def debt_program(DUE):
    while True:
        coin = prompt_coin(DUE)
        DUE -= coin
        if DUE <= 0:
            print(f"Change Owed: {abs(DUE)}")
            break
        else:
            print_amount_due(DUE)

def prompt_coin(DUE):
    user_coin = int(input("Insert Coin: "))
    while user_coin not in [25, 10, 5]:
            print_amount_due(DUE)
            user_coin = int(input("Insert Coin: "))
    return user_coin

def print_amount_due(due):
    print(f"Amount Due: {due}")

if "__main__" == __name__:
    main()