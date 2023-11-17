def convert(input_str):
    print(input_str.replace(":)", "🙂").replace(":(", "🙁"))

if __name__ == "__main__":
    input_str = str(input())
    convert(input_str)