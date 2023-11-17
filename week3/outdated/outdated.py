MONTHS = {"january": 1,
          "february": 2,
          "march": 3,
          "april": 4,
          "may": 5,
          "june": 6,
          "july": 7,
          "august": 8,
          "september": 9,
          "october": 10,
          "november": 11,
          "december": 12}

def main():
    while True:
        input_date = input("Date: ")
        if validate_input(input_date):
             print(validate_input(input_date))
             break
        else:
            continue

def format_date(year, month, day):
    if 1 <= month <= 12 and 1 <= day <= 31:
        return f"{year}-{month:02d}-{day:02d}"
    else:
        return False

def validate_input(input_date):
    slash_input = input_date.split("/")
    comma_input = input_date.split(",")

    try:
        if len(slash_input) == 3:
            month, day, year = int(slash_input[0]), int(slash_input[1]), int(slash_input[2])
            return format_date(year, month, day)
        elif len(comma_input) == 2:
            year = int(comma_input[-1])
            month, day = comma_input[0].split(" ")
            month = month.lower()
            if month in MONTHS:
                return format_date(year, MONTHS[month], int(day))
            else:
                return False
        else:
            return False
    except:
        return False



if "__main__" == __name__:
    main()