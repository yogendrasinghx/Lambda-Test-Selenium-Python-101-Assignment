from selenium.webdriver.common.by import By
from pageObjects.DragDropSliders import DragDropSliders
from pageObjects.InputFormSubmit import InputFormSubmit
from pageObjects.SimpleFormDemo import SimpleFormDemo
from tests.conftest import change_test_status

class SeleniumPlaygroundPage:
    def __init__(self, driver):
        self.driver = driver

    simple_form_demo_link = (By.LINK_TEXT, "Simple Form Demo")
    drag_and_drop_slider_link = (By.LINK_TEXT, "Drag & Drop Sliders")
    input_form_submit_link = (By.XPATH, "//a[normalize-space()='Input Form Submit']")

    def open_playground(self):
        self.driver.get("https://www.lambdatest.com/selenium-playground")

    def click_simple_form_demo(self):
        self.driver.find_element(*SeleniumPlaygroundPage.simple_form_demo_link).click()
        simpleFormDemo = SimpleFormDemo(self.driver)
        return simpleFormDemo

    def click_drag_drop_sliders(self):
        self.driver.find_element(*SeleniumPlaygroundPage.drag_and_drop_slider_link).click()
        dragDropPage = DragDropSliders(self.driver)
        return dragDropPage

    def click_input_form_submit(self):
        self.driver.find_element(*SeleniumPlaygroundPage.input_form_submit_link).click()
        inputFormDemo = InputFormSubmit(self.driver)
        return inputFormDemo
