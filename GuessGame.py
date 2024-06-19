import random

def get_difficulty():
    difficulty = 0
    while difficulty < 1:
        try:
            difficulty = int(input("Enter difficulty level (greater than or equal to 1): "))
            if difficulty < 1:
                print("Invalid difficulty level. Please enter a number greater than or equal to 1.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return difficulty

def get_guess_from_user(difficulty):
    guess = 0
    while guess not in range(1, difficulty + 1):
        try:
            guess = int(input(f"Guess a number between 1 and {difficulty}: "))
            if guess not in range(1, difficulty + 1):
                print(f"Please enter a number between 1 and {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return guess

def compare_results(guess, secret_number):
    return guess == secret_number

def play_game():
    difficulty = get_difficulty()
    secret_number = random.randint(1, difficulty)
    guess = get_guess_from_user(difficulty)

    if compare_results(guess, secret_number):
        print("Congratulations! You guessed the correct number.")
    else:
        print(f"Sorry, the correct number was {secret_number}.")

# Run the game
# play_game()
