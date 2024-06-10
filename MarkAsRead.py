from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, WebDriverException
import time

# Update this path to where chromedriver is located on your system
driver_path = '/path/to/chromedriver'  # Replace with your chromedriver path

# Placeholder for webmail login URL
webmail_url = 'https://your-webmail-login-url.com'  # Replace with your webmail login URL

def wait_for_manual_login():
    input("Please log in manually and then press Enter here to continue...")
    print("Pausing for 5 seconds to allow you to focus on the browser window...")
    time.sleep(5)  # Delay to allow you to focus on the browser window

def mark_emails_as_read(driver):
    try:
        while True:
            # Wait for the email list to load
            select_all_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span.iconCheckbox'))
            )
            print("Checkbox for selecting all emails found.")
            driver.save_screenshot('checkbox_found.png')

            # Ensure the checkbox is interactable
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.iconCheckbox'))
            )

            # Select all emails
            if not select_all_checkbox.is_selected():
                select_all_checkbox.click()
                print("All emails selected.")
                driver.save_screenshot('emails_selected.png')

            # Click on "Mark as Read"
            mark_as_read_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-bind="click: handler, enable: enabled, css: classes, trackClick: track"]//span[contains(text(), "Mark as read")]'))
            )
            mark_as_read_button.click()
            print("Clicked 'Mark as read'.")
            driver.save_screenshot('mark_as_read_clicked.png')

            # Click the next page button
            next_page_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.icon-forward-arrow'))
            )
            next_page_button.click()
            print("Clicked next page.")
            driver.save_screenshot('next_page_clicked.png')

            # Delay to allow the next page to load
            time.sleep(3.5)

            # Wait for the new set of emails to load
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span.iconCheckbox'))
            )
            print("Next page loaded.")
            driver.save_screenshot('next_page_loaded.png')

    except TimeoutException as e:
        print("No more pages to process or timeout occurred.")
        driver.save_screenshot('timeout_error.png')
    except NoSuchElementException as e:
        print(f"Element not found: {e}")
        driver.save_screenshot('no_such_element_error.png')
    except ElementNotInteractableException as e:
        print(f"Element not interactable: {e}")
        driver.save_screenshot('element_not_interactable_error.png')
    except WebDriverException as e:
        print(f"WebDriverException: {e}")
        driver.save_screenshot('webdriver_exception_error.png')

if __name__ == "__main__":
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    try:
        driver.get(webmail_url)
        wait_for_manual_login()
        mark_emails_as_read(driver)
    finally:
        driver.quit()
