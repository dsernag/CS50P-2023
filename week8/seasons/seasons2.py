from datetime import date, datetime
import sys
import inflect

def main():
    input_date = input("Dathe of Birth: ")
    valid_date = validate_date(input_date)
    # print(type(valid_date))
    today = date.today()
    # # today = date(2000,1,1)
    diff = round((today - valid_date).total_seconds() / 60)
    print(number_to_words(diff))
    # print(diff)

def number_to_words(number):
    inflect_eng = inflect.engine()
    return f"{inflect_eng.number_to_words(number, andword = "").capitalize()} minutes"

def validate_date(string, date_format = '%Y-%m-%d'):
    try:
        return date.fromisoformat(string)
        # return datetime.strptime(string, date_format).date()
    except:
        sys.exit("Invalidad date")

if __name__ == "__main__":
    main()