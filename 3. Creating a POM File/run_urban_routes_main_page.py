from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from urban_routes_main_page import UrbanRoutesPage


def test_custom_bike_option():
    
    driver = webdriver.Chrome()
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    driver.get("https://cnt-1559d7a4-e9f5-49d2-a568-67515da435b6.containerhub.tripleten-services.com")

    urban_routes_page = UrbanRoutesPage(driver)

    # Wait for page to load before interacting
    wait.until(EC.visibility_of_element_located((By.ID, "from")))

    urban_routes_page.enter_from_location("East 2nd Street, 601")
    urban_routes_page.enter_to_location("1300 1st St")

    urban_routes_page.click_custom_option()

    # Wait until bike icon becomes clickable
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "your-bike-icon-locator")))
    urban_routes_page.click_bike_icon()

    # Wait until bike text appears
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "your-bike-text-locator")))

    actual_value = urban_routes_page.get_bike_text()
    expected_value = "Bike"

    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    driver.quit()
