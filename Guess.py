import random

class GuessGame:
    def __init__(self):
        self.difficulty = self.get_difficulty()
        self.secret_number = random.randint(1, self.difficulty)

    def get_difficulty(self):
        difficulty = 0
        while difficulty < 1:
            try:
                difficulty = int(input("Enter difficulty level (greater than or equal to 1): "))
                if difficulty < 1:
                    print("Invalid difficulty level. Please enter a number greater than or equal to 1.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        return difficulty

    def get_guess_from_user(self):
        guess = 0
        while guess not in range(1, self.difficulty + 1):
            try:
                guess = int(input(f"Guess a number between 1 and {self.difficulty}: "))
                if guess not in range(1, self.difficulty + 1):
                    print(f"Please enter a number between 1 and {self.difficulty}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        return guess

    def compare_results(self, guess):
        return guess == self.secret_number

    def play(self):
        guess = self.get_guess_from_user()
        if self.compare_results(guess):
            print("Congratulations! You guessed the correct number.")
        else:
            print(f"Sorry, the correct number was {self.secret_number}.")

# Run the game
if __name__ == "__main__":
    game = GuessGame()
    game.play()
