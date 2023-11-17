from datetime import date
import re
import sys
import inflect

def main():
    birth = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(birth)
    except:
        sys.exit("Invalid Date")

    date_birth = date(int(year), int(month), int(day))
    today = date.today()
    diff = today - date_birth
    minutes = diff.days * 24 * 60
    p = inflect.engine()
    output = p.number_to_words(minutes, andword = "")
    print(f"{output.capitalize()} minutes")

def check_birthday(birthday):
    if re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', birthday):
        return birthday.split("-")

if __name__ == "__main__":
    main()

