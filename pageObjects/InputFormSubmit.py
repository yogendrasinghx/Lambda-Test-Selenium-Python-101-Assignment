from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import change_test_status


class InputFormSubmit:
    def __init__(self, driver):
        self.driver = driver

    input_form_submit_link = (By.XPATH, "//a[normalize-space()='Input Form Submit']")
    submit_button = (By.XPATH, "//button[normalize-space()='Submit']")
    name_field = (By.NAME, "name")
    email_field = (By.CSS_SELECTOR, "#inputEmail4")
    password_field = (By.XPATH, "//input[@type='password']")
    company_field = (By.ID, "company")
    website_field = (By.CSS_SELECTOR, "input[placeholder='Website']")
    country_dropdown = (By.NAME, "country")
    city_field = (By.XPATH, "//input[@id='inputCity']")
    address_field1 = (By.NAME, "address_line1")
    address_field2 = (By.NAME, "address_line2")
    state_field = (By.CSS_SELECTOR, "#inputState")
    zipcode_field = (By.CSS_SELECTOR, "input[placeholder='Zip code']")
    error_message = (By.CSS_SELECTOR, ".alert.alert-danger")
    success_message = (By.CSS_SELECTOR, ".success-msg")
    pop_up_exit_button = (By.XPATH, "//span[@id='exit_popup_close']")

    def click_input_form_submit(self):
        self.driver.find_element(*InputFormSubmit.input_form_submit_link).click()

    def click_submit_button(self):
        self.driver.find_element(*InputFormSubmit.submit_button).click()

    def fill_name(self, name):
        self.driver.find_element(*InputFormSubmit.name_field).send_keys(name)

    def fill_email(self, email):
        self.driver.find_element(*InputFormSubmit.email_field).send_keys(email)

    def fill_password(self, email):
        self.driver.find_element(*InputFormSubmit.password_field).send_keys(email)

    def fill_company(self,company):
        return self.driver.find_element(*InputFormSubmit.company_field).send_keys(company)

    def fill_website(self,website):
        return self.driver.find_element(*InputFormSubmit.website_field).send_keys(website)

    def select_country(self, country):
        country_dropdown = Select(self.driver.find_element(*InputFormSubmit.country_dropdown))
        country_dropdown.select_by_visible_text(country)

    def fill_city(self,city):
        return self.driver.find_element(*InputFormSubmit.city_field).send_keys(city)

    def fill_address1(self,address1):
        return self.driver.find_element(*InputFormSubmit.address_field1).send_keys(address1)

    def fill_address2(self, address2):
        return self.driver.find_element(*InputFormSubmit.address_field2).send_keys(address2)

    def fill_state(self,state):
        return self.driver.find_element(*InputFormSubmit.state_field).send_keys(state)

    def fill_zipcode(self, zipcode):
        return self.driver.find_element(*InputFormSubmit.zipcode_field).send_keys(zipcode)

    def validate_error_message(self, expected_message):
        error_message = self.driver.find_element(*InputFormSubmit.name_field).get_attribute("validationMessage")
        change_test_status(self.driver,error_message == expected_message)
        return error_message == expected_message

    def validate_success_message(self, expected_message):
        success_message = self.driver.find_element(*InputFormSubmit.success_message).text
        change_test_status(self.driver,success_message == expected_message)
        return success_message == expected_message

    def close_popup(self):
        js = '''
            setTimeout(function() {
                var event = new MouseEvent('mouseleave', {view: window, bubbles: true, cancelable: true});
                document.body.dispatchEvent(event);
            }, 1000);
            '''
        self.driver.execute_script(js)
        popup_close_button_locator = InputFormSubmit.pop_up_exit_button
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(popup_close_button_locator))
        popup_close_button_element = self.driver.find_element(*popup_close_button_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(popup_close_button_element).click().perform()
