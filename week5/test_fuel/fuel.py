def main():
    usr_input = input("Fraction: ")
    percentage = convert(usr_input)
    print(gauge(percentage))

def convert(fraction):
    try:
        xx, yy = [int(ii) for ii in fraction.split("/")]
        division = round((xx / yy) * 100, 0)
        if division <= 100:
            return int(round((xx / yy) * 100, 0))
        else:
            raise ValueError()
    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()