from selenium.webdriver.common.by import By
from tests.conftest import change_test_status


class SimpleFormDemo:
    def __init__(self, driver):
        self.driver = driver

    message_textbox = (By.ID, "user-message")
    check_value_button = (By.XPATH, "//button[@id='showInput']")
    show_message = (By.CSS_SELECTOR, "#message")

    def validate_url_contains(self, value):
        assert value in self.driver.current_url

    def enter_message(self, message):
        self.driver.find_element(*SimpleFormDemo.message_textbox).send_keys(message)

    def click_get_checked_value(self):
        self.driver.find_element(*SimpleFormDemo.check_value_button).click()

    def validate_message_displayed(self, expected_message):
        actual_message = self.driver.find_element(*SimpleFormDemo.show_message).text
        change_test_status(self.driver, actual_message == expected_message)
        assert actual_message == expected_message
