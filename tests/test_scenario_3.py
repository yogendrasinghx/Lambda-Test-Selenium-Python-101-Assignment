import pytest
from pageObjects.SeleniumPlaygroundPage import SeleniumPlaygroundPage
from testData.InputFormDemoData import InputFormDemoData


@pytest.mark.usefixtures("driver_init")
@pytest.mark.timeout(20)
class TestScenario3:
    def test_check_empty_form(self, driver_init):
        selenium_playground = SeleniumPlaygroundPage(driver_init)
        selenium_playground.open_playground()

        input_form_submit = selenium_playground.click_input_form_submit()
        input_form_submit.click_submit_button()
        assert input_form_submit.validate_error_message("Please fill in the fields")

    def test_validate_form_success(self,driver_init):
        selenium_playground = SeleniumPlaygroundPage(driver_init)
        selenium_playground.open_playground()

        input_form_submit = selenium_playground.click_input_form_submit()
        input_form_submit.close_popup()
        input_form_submit.fill_name(InputFormDemoData.data['name'])
        input_form_submit.fill_email(InputFormDemoData.data['email'])
        input_form_submit.fill_password(InputFormDemoData.data['password'])
        input_form_submit.fill_company(InputFormDemoData.data['company'])
        input_form_submit.fill_website(InputFormDemoData.data['website'])
        input_form_submit.select_country(InputFormDemoData.data['country'])
        input_form_submit.fill_city(InputFormDemoData.data['city'])
        input_form_submit.fill_address1(InputFormDemoData.data['address1'])
        input_form_submit.fill_address2(InputFormDemoData.data['address2'])
        input_form_submit.fill_state(InputFormDemoData.data['state'])
        input_form_submit.fill_zipcode(InputFormDemoData.data['zipcode'])
        input_form_submit.click_submit_button()
        success_message = "Thanks for contacting us, we will get back to you shortly."
        assert input_form_submit.validate_success_message(success_message)
