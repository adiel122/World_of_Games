import os
import Utils

SCORES_FILE_NAME = "Scores.txt"
POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5

def add_score(difficulty):
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read().strip())
        else:
            current_score = 0

        points = POINTS_OF_WINNING(difficulty)
        new_score = current_score + points

        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))

        print(f"Score updated! Current score: {new_score}")

    except Exception as e:
        print(f"An error occurred while updating the score: {e}")
        return Utils.BAD_RETURN_CODE
