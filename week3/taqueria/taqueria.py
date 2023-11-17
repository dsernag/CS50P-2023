MENU = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

def main():
    debt = 0.0
    while True:
        price = place_order()
        debt += price
        print(f"Total: ${debt:.2f}")

def place_order():
    while True:
        try:
            order = input("Item: ").lower().strip()
            return MENU[order]
        except KeyError:
            pass
        except EOFError:
            print("")
            exit()

if "__main__" == __name__:
    main()

