def main():
    grocery_list = {}
    while True:
        try:
            element = input().lower().strip()
            grocery_list = add_element_list(grocery_list, element)
        except EOFError:
            print_grocery_list(grocery_list)
            exit(0)

def  print_grocery_list(grocery_list):
    sorted_dict = dict(sorted(grocery_list.items()))
    printable_list = [f"{str(value)} {element.upper()}" for element, value in sorted_dict.items()]
    print("\n" + "\n".join(printable_list))

def add_element_list(grocery_list, element):
    if element in grocery_list:
        grocery_list[element] += 1
    else:
        grocery_list[element] = 1
    return grocery_list


if "__main__" == __name__:
    main()

