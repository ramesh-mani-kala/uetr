# Filename: test_orangehrm_login.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Fixture to set up and tear down the browser
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")  # Start browser maximized
    service = Service()  # Make sure chromedriver is in your PATH
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_orangehrm_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Wait for login form to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )

    # Fill in credentials
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for dashboard to appear
    dashboard = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )

    # Assert that dashboard is displayed
    assert dashboard.is_displayed(), "Login failed: Dashboard not displayed"
