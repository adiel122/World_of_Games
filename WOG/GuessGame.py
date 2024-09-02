import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = random.randint(1, self.difficulty)
        self.last_guess = None

    def get_guess_from_user(self):
        guess = 0
        while guess not in range(1, self.difficulty + 1):
            try:
                guess = int(input(f"Guess a number between 1 and {self.difficulty}: "))
                if guess not in range(1, self.difficulty + 1):
                    print(f"Please enter a number between 1 and {self.difficulty}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        self.last_guess = guess  # Store the guess value
        return guess

    def compare_results(self, guess):
        return guess == self.secret_number

    def play(self):
        guess = self.get_guess_from_user()
        if self.compare_results(guess):
            print("Congratulations! You guessed the correct number.")
            return True
        else:
            print(f"Sorry, the correct number was {self.secret_number}.")
            return False
