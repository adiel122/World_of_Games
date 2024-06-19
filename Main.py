import Live
import Guess

#Live
name = input("Enter your name: ")
wog = Live.WorldOfGames(name)
print(wog.welcome())
wog.load_game()

#Guess
game = Guess.GuessGame()
game.play()