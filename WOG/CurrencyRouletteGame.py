import random
import requests

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_money_interval(self, usd_amount):
        """Fetches the current exchange rate and generates the interval for the game."""
        # Get the current exchange rate from USD to ILS
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        rate = data['rates']['ILS']

        # Calculate the correct value in ILS
        value_in_ils = usd_amount * rate

        # Calculate the interval based on difficulty
        lower_bound = value_in_ils - (5 - self.difficulty)
        upper_bound = value_in_ils + (5 - self.difficulty)

        return (lower_bound, upper_bound)

    def get_guess_from_user(self, usd_amount):
        """Prompts the user to guess the value of a given amount of USD in ILS."""
        guess = float(input(f"Guess the value of {usd_amount} USD in ILS: "))
        return guess

    def play(self):
        """Plays the currency roulette game."""
        usd_amount = random.randint(1, 100)
        money_interval = self.get_money_interval(usd_amount)

        guess = self.get_guess_from_user(usd_amount)

        if money_interval[0] <= guess <= money_interval[1]:
            print("Congratulations, you won!")
            return True
        else:
            print(f"Sorry, you lost. The correct value was between {money_interval[0]:.2f} and {money_interval[1]:.2f}.")
            return False

# Example usage
if __name__ == "__main__":
    difficulty_level = int(input("Enter the difficulty level (1-5): "))
    game = CurrencyRouletteGame(difficulty=difficulty_level)
    game.play()
