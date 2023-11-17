import re

CONVERSION_TABLE = {
    "AM" : {
        "12" : "00",
        "1" : "01",
        "2" : "02",
        "3" : "03",
        "4" : "04",
        "5" : "05",
        "6" : "06",
        "7" : "07",
        "8" : "08",
        "9" : "09",
        "10" : "10",
        "11" : "11"},
    "PM" : {
        "12" : "12",
        "1" : "13",
        "2" : "14",
        "3" : "15",
        "4" : "16",
        "5" : "17",
        "6" : "18",
        "7" : "19",
        "8" : "20",
        "9" : "21",
        "10" : "22",
        "11" : "23"}}

def main():
    print(convert(input("Hours: ")))

def convert(string):
    pattern = r"^(\d+):?(\d+)? (AM|PM) to (\d+):?(\d+)? (AM|PM)$"
    if result := re.search(pattern, string, re.IGNORECASE):
        initial = [result[1], result[2], result[3]]
        final = [result[4], result[5], result[6]]
        return f"{parse_dates(initial)} to {parse_dates(final)}"
    else:
        raise ValueError()

def parse_dates(input_lst):
    hour = input_lst[0]
    minute = input_lst[1]
    meridiem = input_lst[2]

    if 1 <= int(hour) <= 12:
        if minute == None:
            return f"{CONVERSION_TABLE[meridiem][hour]}:00"
        elif 0 <= int(minute) < 60:
            return f"{CONVERSION_TABLE[meridiem][hour]}:{minute}"
        else:
            raise ValueError()
    else:
        raise ValueError()

if __name__ == "__main__":
    main()