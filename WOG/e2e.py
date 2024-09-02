from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import sys

def test_scores_service(url):
    try:
        # Set up the WebDriver (this will automatically install the latest version of ChromeDriver)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Open the URL
        driver.get(url)

        # Find the score element by its ID
        score_element = driver.find_element(By.ID, "score")

        # Extract the score and check if it's a number between 1 and 1000
        score = int(score_element.text)
        if 1 <= score <= 1000:
            return True
        else:
            print(f"Score {score} is out of the expected range (1-1000).")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    finally:
        # Close the browser
        driver.quit()
        
        
def main_function():
    url = "http://127.0.0.1:5000"
    test_result = test_scores_service(url)

    if test_result:
        print("Test passed!")
        sys.exit(0)
    else:
        print("Test failed!")
        sys.exit(-1)

if __name__ == "__main__":
    main_function()
