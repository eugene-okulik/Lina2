import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(6)
    return chrome_driver


def test_task2(driver):
    wait = WebDriverWait(driver, 10)
    name = "Alina"
    lastname = "Kosarava"
    email = "mytestemail@test.test"
    phone = "2293333333"
    subject = "Arts"
    address = "Kojeduba 14/24"
    driver.get(" https://demoqa.com/automation-practice-form")
    name_input = driver.find_element(By.ID, "firstName")
    name_input.send_keys(name)
    lastname_input = driver.find_element(By.ID, "lastName")
    lastname_input.send_keys(lastname)
    user_email_input = driver.find_element(By.ID, "userEmail")
    user_email_input.send_keys(email)
    gender_input = driver.find_element(By.ID, "gender-radio-2")
    gender_input.click()
    phone_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Mobile Number"]')
    phone_input.send_keys(phone)
    driver.find_element(By.ID, "dateOfBirthInput").click()
    Select(
        driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    ).select_by_visible_text("June")
    Select(
        driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
    ).select_by_visible_text("1998")

    driver.find_element(
        By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='24']"
    ).click()
    subject_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "subjectsInput"))
    )
    subject_input.click()
    subject_input.send_keys(subject)
    wait.until(EC.element_to_be_clickable((By.ID, "react-select-2-option-0"))).click()
    hobbies_input = driver.find_element(By.ID, "hobbies-checkbox-2")
    hobbies_input.click()
    address_input = driver.find_element(By.ID, "currentAddress")
    address_input.send_keys(address)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Без этого слипа вообще никак
    time.sleep(3)
    driver.find_element(By.ID, "state").click()
    driver.find_element(By.XPATH, "//div[text()='Haryana']").click()
    driver.find_element(By.ID, "city").click()
    driver.find_element(By.XPATH, "//div[text()='Karnal']").click()
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    rows = driver.find_elements(By.CSS_SELECTOR, ".table-responsive tbody tr")
    for row in rows:
        key = row.find_element(By.TAG_NAME, "td").text
        value = row.find_elements(By.TAG_NAME, "td")[1].text
        print(f"{key}: {value}")
