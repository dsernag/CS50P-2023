def main():
    time_sex = input("What time is it? ")
    time_dec = convert(time_sex)

    if 7 <= time_dec <= 8:
        print("breakfast time")
    elif 12 <= time_dec <= 13:
        print("lunch time")
    elif 18 <= time_dec <= 19:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + (float(minutes) / 60)

if __name__ == "__main__":
    main()

