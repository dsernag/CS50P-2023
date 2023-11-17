import random as rnd

def main():
    level = prompt_user("Level: ")
    selected_number = generate_rnd_nmb(level)
    guess_number = prompt_user("Guess: ")
    validate_numbers(selected_number, guess_number)

def validate_numbers(selected_number, guess_number):
    if selected_number == guess_number:
        print("Just right!")
    elif guess_number > selected_number:
        print("Too large!")
        guess_number = prompt_user("Guess: ")
        validate_numbers(selected_number, guess_number)
    else:
        print("Too small!")
        guess_number = prompt_user("Guess: ")
        validate_numbers(selected_number, guess_number)

def generate_rnd_nmb(level):
    return rnd.choice(range(1, level + 1))

def prompt_user(message):
    while True:
        try:
            number = int(input(message))
            if number <= 0:
                continue
            else:
                return number
        except:
            continue

if "__main__" == __name__:
    main()