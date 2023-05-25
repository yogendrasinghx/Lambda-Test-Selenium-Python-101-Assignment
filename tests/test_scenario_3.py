import time

from pageObjects.InputFormDemo import InputFormDemo
from pageObjects.PlayGroundPage import PlayGroundPage
from testData.InputFormDemoData import InputFormDemoData
from utilities.BaseClass import BaseClass


class TestScenario3(BaseClass):
    inputFormDemo = None

    def test_scenario_3_a(self):
        global inputFormDemo
        driver = self.driver
        playGroundPage = PlayGroundPage(driver)
        inputFormDemo = playGroundPage.click_input_form_submit_link()

        inputFormDemo.get_submit_button().click()

        message = inputFormDemo.getRequiredMessage()

        assert message == "Please fill in the fields"

    def test_scenario_3_b(self):
        inputFormDemo.get_name_field().send_keys(InputFormDemoData.data['name'])
        inputFormDemo.get_email_field().send_keys(InputFormDemoData.data['email'])
        inputFormDemo.get_website_field().send_keys(InputFormDemoData.data['website'])
        inputFormDemo.get_password_field().send_keys(InputFormDemoData.data['password'])
        inputFormDemo.get_company_field().send_keys(InputFormDemoData.data['company'])
        inputFormDemo.get_city_field().send_keys(InputFormDemoData.data['city'])
        inputFormDemo.get_state_field().send_keys(InputFormDemoData.data['state'])
        inputFormDemo.get_address_field1().send_keys(InputFormDemoData.data['address1'])
        inputFormDemo.get_address_field2().send_keys(InputFormDemoData.data['address2'])
        inputFormDemo.get_zipcode_field().send_keys(InputFormDemoData.data['zipcode'])

        inputFormDemo.select_country_field(InputFormDemoData.data['country'])

        inputFormDemo.get_submit_button().click()

        submit_message = InputFormDemoData.data['submit_message']

        assert submit_message == inputFormDemo.get_submit_message().text

