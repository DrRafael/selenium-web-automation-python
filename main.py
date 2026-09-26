import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Configuration and Environment Variables
BASE_URL = os.environ.get("BASE_URL", "https://platform.kodland.org/auth/")
TASK_URL = os.environ.get("TASK_URL", "https://platform.kodland.org/ru/task_57407/")
USER_LOGIN = os.environ.get("USER_LOGIN", "YOUR_LOGIN")
USER_PASSWORD = os.environ.get("USER_PASSWORD", "YOUR_PASSWORD")


def run_automation_flow():
    """Automates user login and task completion workflow using Selenium WebDriver."""
    # Initialize Chrome Driver using modern Service manager
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    wait = WebDriverWait(driver, timeout=10)

    try:
        # Step 1: Open authentication page
        driver.get(BASE_URL)

        # Step 2: Locate elements using Explicit Waits
        login_input = wait.until(EC.presence_of_element_located((By.NAME, "login")))
        password_input = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.TAG_NAME, "button")

        # Step 3: Perform authentication
        login_input.send_keys(USER_LOGIN)
        password_input.send_keys(USER_PASSWORD)
        submit_button.click()

        # Step 4: Navigate to task page
        wait.until(EC.url_changes(BASE_URL))
        driver.get(TASK_URL)

        # Step 5: Execute automated task completion steps
        for step in range(6):
            sub_button = wait.until(EC.element_to_be_clickable((By.ID, "sub-button")))
            sub_button.click()

            ok_button = wait.until(EC.element_to_be_clickable((By.ID, "submit_task_button")))
            ok_button.click()

            next_button = wait.until(EC.element_to_be_clickable((By.ID, "next_task_button")))
            next_button.click()

            print(f"[QA Log] Step {step + 1} completed successfully.")

    except Exception as e:
        print(f"[QA Error] Test execution failed: {str(e)}")

    finally:
        # Step 6: Gracefully close browser session
        driver.quit()


if __name__ == "__main__":
    run_automation_flow()
