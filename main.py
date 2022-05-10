from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = r"C:\Users\jithe\Downloads\chromedriver_win32\chromedriver.exe"

s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)
url = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102713980&keywords=python%20developer&location=India"

driver.get(url=url)

sign_in_button = driver.find_element(by=By.CLASS_NAME, value="nav__button-secondary")

sign_in_button.click()

email_field = driver.find_element(by=By.NAME, value="session_key")
email_field.send_keys("XXXX@gmail.com")

password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys("XXXXX")

sign_in = driver.find_element(by=By.CSS_SELECTOR, value="form button")
sign_in.send_keys(Keys.ENTER)

apply_job_posts = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in apply_job_posts:
    print("Clicked Easy_apply confirmed")
    listing.click()
    time.sleep(3)

    try:
        # apply button field
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # phone number field
        phone_number = driver.find_element(by=By.CLASS_NAME, value="fb-single-line-text__input")
        if phone_number.text == "":
            phone_number.send_keys("1234567899")

        # Cancel and discard button
        cancel_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        cancel_button.click()

        discard_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")
        discard_button.click()

    except NoSuchElementException:
        print("No Application button available, skipped")
        continue

driver.quit()
