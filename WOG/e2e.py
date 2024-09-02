# e2e.py

from selenium import webdriver
import sys
import time

def test_scores_service(url):
    """Test if the score on the web service is between 1 and 1000."""
    # Initialize the browser (this example uses Chrome)
    driver = webdriver.Chrome()  # You might need to specify the path to your webdriver
    driver.get(url)

    time.sleep(2)  # Allow some time for the page to load

    try:
        # Find the score element by its ID
        score_element = driver.find_element_by_id("score")
        score = int(score_element.text)

        # Check if the score is between 1 and 1000
        if 1 <= score <= 1000:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()

def main_function():
    url = "http://0.0.0.0:5000" 
    test_result = test_scores_service(url)

    if test_result:
        print("Test passed!")
        sys.exit(0)
    else:
        print("Test failed!")
        sys.exit(-1)

if __name__ == "__main__":
    main_function()
