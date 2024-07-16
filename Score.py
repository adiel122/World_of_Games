import os
import Utils as utils

SCORES_FILE_NAME = "Scores.txt"
POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5

def add_score(difficulty):
    """
    Adds the score based on the difficulty level to the scores file.
    If the file does not exist, it creates a new one.
    """
    try:
        # Try to read the current score from the file
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read().strip())
        else:
            current_score = 0

        # Calculate the new score
        points = POINTS_OF_WINNING(difficulty)
        new_score = current_score + points

        # Write the new score back to the file
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))

        print(f"Score updated! Current score: {new_score}")

    except Exception as e:
        print(f"An error occurred while updating the score: {e}")
        return utils.BAD_RETURN_CODE

if __name__ == "__main__":
    # Example usage
    difficulty_level = int(input("Enter the difficulty level: "))
    add_score(difficulty_level)
