def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 0.7 seconds and you have to recall them.")
    print("2. Guess Game - guess a number and see if you chose like the computer.")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS.")

    game_choice = int(input("Enter the number of the game you want to play: "))
    difficulty = int(input("Choose difficulty level (1-5): "))

    if game_choice == 1:
        from MemoryGame import MemoryGame
        game = MemoryGame(difficulty)
    elif game_choice == 2:
        from GuessGame import GuessGame  # Assuming you have a GuessGame implemented elsewhere
        game = GuessGame(difficulty)
    elif game_choice == 3:
        from CurrencyRouletteGame import CurrencyRouletteGame
        game = CurrencyRouletteGame(difficulty)
    else:
        print("Invalid choice.")
        return

    game.play()

if __name__ == "__main__":
    load_game()