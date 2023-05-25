import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass


class InputFormDemo():
    def __init__(self,driver):
        self.driver = driver

    submit_button = (By.XPATH, "//button[normalize-space()='Submit']")
    name_field = (By.NAME, "name")
    email_field = (By.CSS_SELECTOR, "#inputEmail4")
    password_field = (By.XPATH, "//input[@type='password']")
    company_field = (By.ID, "company")
    website_field = (By.CSS_SELECTOR, "input[placeholder='Website']")
    country_field = (By.NAME, "country")
    city_field = (By.XPATH, "//input[@id='inputCity']")
    address_field1 = (By.NAME, "address_line1")
    address_field2 = (By.NAME, "address_line2")
    state_field = (By.CSS_SELECTOR, "#inputState")
    zipcode_field = (By.CSS_SELECTOR, "input[placeholder='Zip code']")
    submit_message = (By.CSS_SELECTOR, ".success-msg")


    def get_submit_button(self):
        return self.driver.find_element(*InputFormDemo.submit_button)

    def getRequiredMessage(self):
        message = self.driver.find_element(*InputFormDemo.name_field).get_attribute("validationMessage")
        return message

    def get_name_field(self):
        return self.driver.find_element(*InputFormDemo.name_field)

    def get_email_field(self):
        return self.driver.find_element(*InputFormDemo.email_field)

    def get_password_field(self):
        return self.driver.find_element(*InputFormDemo.password_field)

    def get_company_field(self):
        return self.driver.find_element(*InputFormDemo.company_field)

    def get_website_field(self):
        return self.driver.find_element(*InputFormDemo.website_field)

    def get_country_field(self):
        return self.driver.find_element(*InputFormDemo.country_field)

    def get_city_field(self):
        return self.driver.find_element(*InputFormDemo.city_field)

    def get_address_field1(self):
        return self.driver.find_element(*InputFormDemo.address_field1)

    def get_address_field2(self):
        return self.driver.find_element(*InputFormDemo.address_field2)

    def get_state_field(self):
        return self.driver.find_element(*InputFormDemo.state_field)

    def get_zipcode_field(self):
        return self.driver.find_element(*InputFormDemo.zipcode_field)

    def select_country_field(self,country):
        select = Select(self.driver.find_element(*InputFormDemo.country_field))
        select.select_by_visible_text(country)

    def get_submit_message(self):
        return self.driver.find_element(*InputFormDemo.submit_message)

