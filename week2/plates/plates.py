import string
def main():
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):

    # 1) Between 6 and 2 characters
    if not 2 <= len(plate) <= 6:
        return False
    # 2) No puctuation or spaces
    elif any(letter in string.punctuation for letter in plate):
        return False
    # 3) Start with 2 letters
    elif any(letter not in string.ascii_uppercase for letter in plate[:2]):
        return False
    # 4) Numbers cannot be used in the middle of a plate; they must come at the end
    elif plate[-1].isnumeric() and plate[-2] in string.ascii_uppercase:
        return False
    # 5) Numbers cannot start by 0
    else:
        try:
            numbers = [ii for ii in plate if ii.isnumeric()]
            if numbers[0] == "0":
                return False
            else:
                return True
        except:
            return True

if "__main__" == __name__:
    main()