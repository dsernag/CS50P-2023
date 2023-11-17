import random

def main():
    score = 0

    level = get_level()
    for _ in range(1, 11):
        number1, number2, answer = generate_problem(level)
        score = validate_problem(score, answer, number1, number2)
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0 or level > 3:
                continue
            else:
                return level
        except ValueError:
            continue
        except EOFError:
            exit(0)

# https://blog.finxter.com/python-how-to-generate-a-random-number-with-a-specific-amount-of-digits/#:~:text=Shortest%20Solution%20with%20randint()&text=The%20easiest%20way%20to%20create,randint(1000%2C9999)%20.
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    else:
        return random.randint(int('1' + '0' * (level - 1)), int('9' * level))

def generate_problem(level):
    number1 = generate_integer(level)
    number2 = generate_integer(level)
    answer = number1 + number2
    return number1, number2, answer

def validate_problem(score, answer, number1, number2):
    errors = 0
    base_msn = f'{number1} + {number2} = '
    for _ in range(0, 3):
        try:
            guest_number = int(input(base_msn))
            if guest_number == answer:
                score += 1
                break
            else:
                print("EEE")
                errors += 1
        except ValueError:
            print("EEE")
            errors +=1
            continue
        except EOFError:
            exit(0)
    if errors == 3:
        print(f"{base_msn} {answer}")
        return score
    else:
        return score

if __name__ == "__main__":
    main()