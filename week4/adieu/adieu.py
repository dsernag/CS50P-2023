import inflect

def main():
    lst_names = []
    while True:
        try:
            usr_input = input("Name: ")
            lst_names.append(usr_input)
        except EOFError:
            base_msn = "Adieu, adieu, to "
            print(base_msn + inflect.engine().join(lst_names))
            break

if "__main__" == __name__:
    main()