import requests
import sys

def main():
    amount = validate_argv()
    btc_price = btc_value()
    print(f"${amount * btc_price:,.4f}")

def btc_value():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        json_response = response.json()
        return float((json_response["bpi"]["USD"]["rate"]).replace(",", ""))
    except requests.RequestException:
        sys.exit("Something went wrong =(")

def validate_float(str_number):
     try:
          return float(str_number)
     except:
        return False

def validate_argv():
    args = sys.argv
    if len(args) < 2 or len(args) == 1 or len(args) > 2:
        sys.exit("Missing command-line argument")
    elif validate_float(args[1]):
        return validate_float(args[1])
    else:
        sys.exit("Command-line argument is not a number")

if "__main__" == __name__:
    main()