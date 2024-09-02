import random
import time

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        """Generates a list of random numbers between 1 and 101 with length equal to difficulty."""
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        """Prompts the user to input a list of numbers. The list length is equal to difficulty."""
        print(f"Please enter {self.difficulty} numbers separated by spaces:")
        user_input = input()
        # Convert the input string to a list of integers
        return [int(num) for num in user_input.split()]

    def is_list_equal(self, list1, list2):
        """Compares two lists and returns True if they are equal, False otherwise."""
        return list1 == list2

    def play(self):
        """Plays the memory game."""
        # Generate the sequence and display it to the user
        sequence = self.generate_sequence()
        print("Remember this sequence:")
        print(sequence)
        # Display the sequence for 0.7 seconds
        time.sleep(0.7)
        # Clear the screen (in most terminals, this might work; if not, it will just print new lines)
        print("\033c", end="")

        # Get the sequence from the user
        user_sequence = self.get_list_from_user()

        # Compare the user's sequence with the generated sequence
        if self.is_list_equal(sequence, user_sequence):
            print("Congratulations, you won!")
            return True
        else:
            print("Sorry, you lost.")
            return False

# Example usage
if __name__ == "__main__":
    difficulty_level = int(input("Enter the difficulty level (number of digits to remember): "))
    game = MemoryGame(difficulty=difficulty_level)
    game.play()
