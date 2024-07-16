import os
import platform

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

def screen_cleaner():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    print(f"Scores will be saved in: {SCORES_FILE_NAME}")
    print(f"Bad return code is set to: {BAD_RETURN_CODE}")
    input("Press Enter to clear the screen...")
    screen_cleaner()
    print("Screen cleared.")
