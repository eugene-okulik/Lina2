import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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
    wait = WebDriverWait(driver, 10)
    driver.get("http://testshop.qa-practice.com/")
    link = driver.find_element(By.XPATH, "//a[@content='Customizable Desk']")
    ActionChains(driver).key_down(Keys.COMMAND).click(link).key_up(
        Keys.COMMAND
    ).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.find_element(By.ID, "add_to_cart_wrap").click()
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-secondary"))
    )
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-secondary").click()
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.CLASS_NAME, "o_wsale_my_cart").click()
    driver.find_element(By.ID, "cart_products")
    time.sleep(3)


def test_task2(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://testshop.qa-practice.com/")
    link = driver.find_element(By.CLASS_NAME, "oe_product")
    cart = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.a-submit")
    ActionChains(driver).move_to_element(link).move_to_element(cart).click().perform()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
    driver.find_element(By.CSS_SELECTOR, ".product-name.product_display_name")
