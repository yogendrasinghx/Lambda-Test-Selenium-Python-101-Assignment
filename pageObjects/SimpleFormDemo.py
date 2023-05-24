from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class SimpleFormDemo(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    message_textbox = (By.ID, "user-message")
    check_value_button = (By.XPATH, "//button[@id='showInput']")
    show_message = (By.CSS_SELECTOR, "#message")

    def get_message_textbox(self):
        return self.driver.find_element(*SimpleFormDemo.message_textbox)

    def get_check_value_button(self):
        return self.driver.find_element(*SimpleFormDemo.check_value_button)

    def get_show_message(self):
        return self.driver.find_element(*SimpleFormDemo.show_message)