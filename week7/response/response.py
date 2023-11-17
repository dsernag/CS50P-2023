import validators

def main():
    print(validate_email(input("What's your email address? ")))

def validate_email(string):
    if validators.email(string):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()