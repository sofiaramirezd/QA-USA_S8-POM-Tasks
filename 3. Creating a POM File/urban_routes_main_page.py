from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:

    # Locators
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    BIKE_ICON_LOCATOR = ...
    BIKE_TEXT_LOCATOR = ...

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_from_location(self, from_text):
        from_input = self.wait.until(
            EC.visibility_of_element_located(self.FROM_LOCATOR)
        )
        from_input.clear()
        from_input.send_keys(from_text)

    def enter_to_location(self, to_text):
        to_input = self.wait.until(
            EC.visibility_of_element_located(self.TO_LOCATOR)
        )
        to_input.clear()
        to_input.send_keys(to_text)

    def click_custom_option(self):
        custom_button = self.wait.until(
            EC.element_to_be_clickable(self.CUSTOM_OPTION_LOCATOR)
        )
        custom_button.click()

    def click_bike_icon(self):
        bike_icon = self.wait.until(
            EC.element_to_be_clickable(self.BIKE_ICON_LOCATOR)
        )
        bike_icon.click()

    def get_bike_text(self):
        bike_text = self.wait.until(
            EC.visibility_of_element_located(self.BIKE_TEXT_LOCATOR)
        )
        return bike_text.text
