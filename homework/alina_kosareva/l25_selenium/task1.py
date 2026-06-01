from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(6)
    # chrome_driver.maximize_window()
    # chrome_driver.set_window_size(1300, 1080)
    return chrome_driver


def test_task1(driver):
    input_data = "my_test_text"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_string_input = driver.find_element(By.ID, "id_text_string")
    text_string_input.send_keys(input_data)
    text_string_input.send_keys(Keys.ENTER)
    result = driver.find_element(By.ID, "result-text")
    assert result.text == input_data
    print(result.text)
