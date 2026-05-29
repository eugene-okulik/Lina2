from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def test_task3_part1(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    language_list = Select(driver.find_element(By.ID, "id_choose_language"))
    language_list.select_by_visible_text("Python")
    submit_button = driver.find_element(By.ID, "submit-id-submit")
    submit_button.click()
    result = driver.find_element(By.ID, "result-text")
    assert result.text == "Python"


def test_task3_part2(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()
    finish = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    assert finish.text == "Hello World!"
