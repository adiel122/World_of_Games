import os
import platform

# Constants
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

# Function to clear the screen
def screen_cleaner():
    # Clear command as a function of OS
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    # Example usage
    print(f"Scores will be saved in: {SCORES_FILE_NAME}")
    print(f"Bad return code is set to: {BAD_RETURN_CODE}")
    input("Press Enter to clear the screen...")
    screen_cleaner()
    print("Screen cleared.")
